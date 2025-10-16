const form = document.getElementById('upload-form');
const resultDiv = document.getElementById('result');
const imageInput = document.getElementById('image-input');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!imageInput.files[0]) return;

    const file = imageInput.files[0];

    // Show uploaded image preview
    const reader = new FileReader();
    reader.onload = function(e) {
        resultDiv.innerHTML = `<img src="${e.target.result}" alt="Uploaded Image">`;
    }
    reader.readAsDataURL(file);

    // Send file via fetch
    const formData = new FormData();
    formData.append('image', file);

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            body: formData
        });
        const data = await response.json();
        resultDiv.innerHTML += `<h3>Prediction: ${data.prediction}</h3>
                                <p>Probability (Tumor): ${data.probability}</p>`;
    } catch (err) {
        resultDiv.innerHTML += `<p style="color:red">Error: ${err}</p>`;
    }
});
