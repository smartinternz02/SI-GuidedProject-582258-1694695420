const form = document.getElementById("prediction-form");
const resultDiv = document.getElementById("prediction-result");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    const formData = new FormData(form);
    fetch("/predict", {
        method: "POST",
        body: formData
    })
        .then(response => response.text())
        .then(data => {
            resultDiv.innerHTML = `<h3>Prediction Result: ${data}</h3>`;
        })
        .catch(error => {
            console.error("Error:", error);
        });
});
