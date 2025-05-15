import cv2
import numpy as np
from model_loader import load_trained_model

model = load_trained_model()

def analyze(file_path):
    try:
        cap = cv2.VideoCapture(file_path)

        if not cap.isOpened():
            return {"error": "Could not open video file."}

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        video_duration = frame_count / fps if fps != 0 else 0
        frames_analyzed = min(50, frame_count)
        frames = []
        for _ in range(frames_analyzed):
            ret, frame = cap.read()
            if not ret:
                print("No frame captured at this point.")
                continue
            resized_frame = cv2.resize(frame, (128, 128))
            frames.append(resized_frame)

        cap.release()

        if len(frames) == 0:
            print("No frames were captured. Check video path or format.")
            return {"error": "No frames could be extracted from the video."}

        frames_array = np.array(frames) / 255.0
        print(f"Number of frames for prediction: {len(frames_array)}")

        predictions = model.predict(frames_array)
        predictions = predictions.flatten()
        avg_score = np.mean(predictions)

        confidence = float(np.mean(predictions))
        max_confidence = float(np.max(predictions))
        min_confidence = float(np.min(predictions))
        raw_score = float(avg_score)

        threshold = 0.5
        label = "Fake" if avg_score >= threshold else "Real"
        consistency = "Very Consistent" if confidence > 0.9 else "Inconsistent"

        print(f"Prediction: {label}, Confidence: {confidence}, Raw Score: {raw_score}")

        return {
            "confidence": confidence,
            "consistency": consistency,
            "frames_analyzed": len(frames_array),
            "video_duration": f"{int(video_duration // 60)}:{int(video_duration % 60)}",
            "max_confidence": max_confidence,
            "min_confidence": min_confidence,
            "raw_score": raw_score,
            "label": label
        }

    except Exception as e:
        print(f"Error during analysis: {e}")
        return {"error": str(e)}
