# 🎥 Deepfake Detection System

This is a final-year project that implements a deepfake video classification system using a Convolutional Neural Network (CNN) trained on a small yet balanced dataset. The system allows users to upload a video file and get a prediction on whether it's real or fake based on frame-by-frame analysis.

---

## Getting Started

1. **Clone the repository**
```bash
git clone https://github.com/HasibeeGencc/DeepfakeVideoDetector.git
cd DeepfakeVideoDetector
```

2. **Install required packages**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Visit in browser**  
The app should open automatically, or you can go to:  
`http://127.0.0.1:5000`

---

## 🖥️ How to Use the System (For Users)

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

## 📊 Model Performance Summary

| Metric       | Score  |
|--------------|--------|
| Accuracy     | 95.5%  |
| Precision    | 95.1%  |
| Recall       | 96.0%  |
| F1 Score     | 95.5%  |
| ROC-AUC      | 95.5%  |

Model trained on a balanced set (400 real, 400 fake images), evaluated on 200 test samples.


## 📜 License

This project is part of a final-year capstone at De Montfort University and is shared for educational purposes.