document.addEventListener("DOMContentLoaded", function () {
    const dropZone = document.getElementById('dropZone');
    const fileInput = document.getElementById('fileInput');
    const loading = document.getElementById('loading');
    const resultCard = document.getElementById('resultCard');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const videoName = document.getElementById('videoName');

    let selectedFile = null;

    fileInput.addEventListener('change', handleFileSelect);
    analyzeBtn.addEventListener('click', handleAnalyze);

    function handleFileSelect(e) {
        selectedFile = e.target.files[0];

        if (!selectedFile) {
            analyzeBtn.classList.add('d-none');
            videoName.textContent = '';
            return;
        }

        videoName.textContent = `Selected: ${selectedFile.name}`;
        analyzeBtn.classList.remove('d-none');
    }

    function handleAnalyze() {
        if (!selectedFile) {
            alert("Please select a video file first.");
            return;
        }

        uploadFile(selectedFile);
    }

    function uploadFile(file) {
        const formData = new FormData();
        formData.append('videoFile', file);

        loading.style.display = 'block';
        resultCard.style.display = 'none';
        analyzeBtn.classList.add('d-none');

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            loading.style.display = 'none';

            if (data.error) {
                alert(`Error: ${data.error}`);
                return;
            }

            displayResults(data.analysis);
        })
        .catch(error => {
            console.error('Error:', error);
            loading.style.display = 'none';
        });
    }

    function displayResults(data) {
        resultCard.style.display = 'block';
        document.getElementById('resultTitle').textContent = `Result: ${data.label}`;
        document.getElementById('confidence').textContent = `${(data.confidence * 100).toFixed(2)}%`;
        document.getElementById('consistency').textContent = data.consistency;
        document.getElementById('framesAnalyzed').textContent = data.frames_analyzed;
        document.getElementById('duration').textContent = data.video_duration;
        document.getElementById('maxConfidence').textContent = `${(data.max_confidence * 100).toFixed(2)}%`;
        document.getElementById('minConfidence').textContent = `${(data.min_confidence * 100).toFixed(2)}%`;
        document.getElementById('rawScore').textContent = `${(data.raw_score * 100).toFixed(2)}%`;
    }
});
