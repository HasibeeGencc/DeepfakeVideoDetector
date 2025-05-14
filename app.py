from flask import Flask, render_template, request, jsonify
import os
import webbrowser
from analyze_video import analyze

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'videoFile' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['videoFile']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Analyze the uploaded video
    analysis_result = analyze(filepath)

    # Konsola yazdır - Debugging için
    print(f"Analysis Result: {analysis_result}")

    # Eğer 'error' varsa hata döndür
    if 'error' in analysis_result:
        return jsonify({"error": analysis_result['error']}), 500

    # Analysis sonucunu kontrol et ve çıktı ver
    if analysis_result['label'] == "Fake":
        print(f"ALERT: Video {file.filename} is classified as FAKE")
    elif analysis_result['label'] == "Real":
        print(f"INFO: Video {file.filename} is classified as REAL")

    return jsonify({"analysis": analysis_result})

if __name__ == '__main__':
    url = "http://127.0.0.1:5000"
    webbrowser.open(url)
    app.run(debug=True)
