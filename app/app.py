from flask import Flask, render_template, request, jsonify
from tensorflow import keras
import joblib
import numpy as np

app = Flask(__name__)

# Load preprocessor and model
preprocessor_path = "artifacts/data_preprocess/text_preprocessor.pkl"
model_path = "artifacts/training/trained_model.h5"

preprocessor = joblib.load(preprocessor_path)
model = keras.models.load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        
        # Preprocess text and make prediction
        text_transformed = preprocessor.transform([text])
        prediction = model.predict(text_transformed)
        
        # Determine if it's human or AI-generated text
        prediction_label = 'Human Text' if prediction[0] < 0.5 else 'AI Generated Text'
        
        return jsonify({'prediction': prediction_label})

if __name__ == '__main__':
    app.run(debug=True)
