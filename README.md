# Deepfake Video Detection System

This project is a deep learning-based system to detect whether a video is **real** or **deepfake (fake)**. It allows users to upload a video file via a web interface and instantly receive predictions powered by a trained CNN model.

---

## Project Overview

- **Goal**: Detect fake videos using a trained Convolutional Neural Network (CNN).
- **Input**: Video file (e.g., `.mp4`, `.avi`)
- **Output**: Real or Fake prediction with confidence and additional metrics
- **Frameworks**: TensorFlow, OpenCV, Flask, HTML/CSS/JS (Bootstrap)

---

## 📁 Project Structure

**Visit in browser**  
The app should open automatically, or you can go to:  
`http://127.0.0.1:5000`

---

## How to Use the System (For Users)

1. **Open the App**  
The interface will open in your default browser.

2. **Upload a Video File**  
- Drag and drop a `.mp4` or other video format into the upload area  
*OR*  
- Click the “Select Video File” button and choose a file from your computer.

3. **Start Analysis**  
- Click on **"Analyze Video"** (if available) or wait for the analysis to start automatically.

4. **View Results**  
- After processing, the result card will display:
  - **Predicted Label**: Real or Fake
  - **Confidence Score**
  - **Frames Analyzed**
  - **Video Duration**
  - **Min/Max Confidence**
  - **Consistency Level**
  - **Raw Model Score**

---


## 📜 License

This project is part of a final-year capstone at De Montfort University and is shared for educational purposes.
