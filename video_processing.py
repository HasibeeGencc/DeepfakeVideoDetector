import cv2
import numpy as np
import os

def extract_frames(video_path, num_blocks=50):
    cap = cv2.VideoCapture(video_path)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frames_per_block = max(1, total_frames // num_blocks)
    frames = []

    for block in range(num_blocks):
        cap.set(cv2.CAP_PROP_POS_FRAMES, block * frames_per_block)
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (128, 128))
        frames.append(resized_frame)

    cap.release()
    frames = np.array(frames)
    np.save('frames.npy', frames)
    print(f"Extracted {len(frames)} frames and saved as frames.npy")

if __name__ == "__main__":
    video_path = "sample_video.mp4"
    extract_frames(video_path)
