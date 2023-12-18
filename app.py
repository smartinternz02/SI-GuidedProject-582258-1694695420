from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load your machine learning model here
# Example: model = pickle.load(open('your_model.pkl', 'rb'))
model = pickle.load(open('shopping.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        page_values = float(request.form['pageValues'])
        special_day = float(request.form['specialDay'])
        month = float(request.form['month'])

        # Perform predictions using your model
        prediction = model.predict([[page_values, special_day, month]])

        # Assuming prediction is a number, you can convert it to a readable format if needed
        prediction_text = f'The predicted result is: {prediction[0]}'  # Replace this with your actual prediction value

        return render_template('index.html', prediction_result=prediction_text)

if __name__ == '__main__':
    app.run(debug=True)
