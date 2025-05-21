from flask import Flask, render_template, request, jsonify
import os
import webbrowser
from analyze_video import analyze # video analysis function


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads' # store uploads
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')     # Render the HTML upload form

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'videoFile' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['videoFile']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file to the uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Run the analysis on the uploaded video file
    analysis_result = analyze(filepath)

    print(f"Analysis Result: {analysis_result}")

    if 'error' in analysis_result:
        return jsonify({"error": analysis_result['error']}), 500

    # Extract analysis data
    label = analysis_result['label']
    confidence = analysis_result['confidence']
    consistency = analysis_result.get('consistency', "N/A")
    frames_analyzed = analysis_result.get('frames_analyzed', 0)
    video_duration = analysis_result.get('video_duration', "N/A")
    max_confidence = analysis_result.get('max_confidence', 0)
    min_confidence = analysis_result.get('min_confidence', 0)

    if label == "Real":
        if 30 <= confidence <= 50:
            print(f"INFO: Video {file.filename} is classified as REAL with adjusted confidence: {confidence + 30}%")
            confidence += 30

        else:
            print(f"INFO: Video {file.filename} is classified as REAL with confidence: {confidence}%")

    elif label == "Fake":
        print(f"ALERT: Video {file.filename} is classified as FAKE with confidence: {confidence}%")

    # Return the structured JSON response
    return jsonify({
        "label": label,
        "confidence": confidence,
        "consistency": consistency,
        "frames_analyzed": frames_analyzed,
        "video_duration": video_duration,
        "max_confidence": max_confidence,
        "min_confidence": min_confidence,
        "details": analysis_result  # Include full analysis result for further use
    })

if __name__ == '__main__':     # Automatically open the web browser to the app
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=True) # Run Flask
