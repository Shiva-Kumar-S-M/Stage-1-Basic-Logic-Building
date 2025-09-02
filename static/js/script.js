document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const uploadArea = document.getElementById('uploadArea');
    const imagePreview = document.getElementById('imagePreview');
    const previewImage = document.getElementById('previewImage');
    const resultContainer = document.getElementById('resultContainer');
    const resultPlaceholder = document.getElementById('resultPlaceholder');
    const resultDetails = document.getElementById('resultDetails');
    const indicatorCircle = document.getElementById('indicatorCircle');
    const resultText = document.getElementById('resultText');
    const confidenceValue = document.getElementById('confidenceValue');
    const meterFill = document.getElementById('meterFill');
    const recommendation = document.getElementById('recommendation');

    // Drag and drop functionality
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        uploadArea.addEventListener(eventName, highlight, false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        uploadArea.addEventListener(eventName, unhighlight, false);
    });

    function highlight() {
        uploadArea.classList.add('highlight');
    }

    function unhighlight() {
        uploadArea.classList.remove('highlight');
    }

    uploadArea.addEventListener('drop', handleDrop, false);
    fileInput.addEventListener('change', handleFileSelect, false);

    function handleDrop(e) {
        const dt = e.dataTransfer;
        const files = dt.files;
        handleFiles(files);
    }

    function handleFileSelect(e) {
        const files = e.target.files;
        handleFiles(files);
    }

    function handleFiles(files) {
        if (files.length === 0) return;
        
        const file = files[0];
        if (!file.type.match('image.*')) {
            alert('Please upload an image file');
            return;
        }

        // Preview image
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            imagePreview.style.display = 'block';
            
            // Upload and analyze image
            uploadAndAnalyze(file);
        };
        reader.readAsDataURL(file);
    }

    function uploadAndAnalyze(file) {
        // Show loading state
        resultPlaceholder.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Analyzing image...</p>
            </div>
        `;
        resultDetails.style.display = 'none';
        resultPlaceholder.style.display = 'block';

        // Create form data
        const formData = new FormData();
        formData.append('file', file);

        // Send to server
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'error') {
                throw new Error(data.error);
            }
            
            displayResult(data);
        })
        .catch(error => {
            resultPlaceholder.innerHTML = `
                <div style="text-align: center; color: #f44336;">
                    <p>Error: ${error.message}</p>
                    <p>Please try again with a different image.</p>
                </div>
            `;
        });
    }

    function displayResult(data) {
        resultPlaceholder.style.display = 'none';
        resultDetails.style.display = 'block';
        
        if (data.result === 'PNEUMONIA') {
            indicatorCircle.className = 'indicator-circle indicator-pneumonia';
            indicatorCircle.innerHTML = '!';
            resultText.textContent = 'Pneumonia Detected';
            meterFill.className = 'meter-fill meter-pneumonia';
            recommendation.innerHTML = `
                <p><strong>Recommendation:</strong> This result suggests possible pneumonia. 
                Please consult with a healthcare professional immediately for further evaluation and treatment.</p>
            `;
        } else {
            indicatorCircle.className = 'indicator-circle indicator-normal';
            indicatorCircle.innerHTML = '✓';
            resultText.textContent = 'Normal - No Pneumonia Detected';
            meterFill.className = 'meter-fill meter-normal';
            recommendation.innerHTML = `
                <p><strong>Recommendation:</strong> No signs of pneumonia detected. 
                However, if you're experiencing symptoms, please consult with a healthcare professional for accurate diagnosis.</p>
            `;
        }
        
        confidenceValue.textContent = `${data.confidence}%`;
        meterFill.style.width = `${data.confidence}%`;
    }

    // Click on upload area to open file dialog
    uploadArea.addEventListener('click', function(e) {
        if (e.target !== fileInput && e.target !== this.querySelector('button')) {
            fileInput.click();
        }
    });
});