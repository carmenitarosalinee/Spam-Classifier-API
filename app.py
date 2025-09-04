from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load model
model = joblib.load("spam_classifier.pkl")

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Spam Classifier API is running!"}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide text"}), 400
    
    text = data["text"]

    input_data = {
        "clean_text": [text],
        "length": [len(text)],
        "word_count": [len(text.split())]
    }
    X_input = pd.DataFrame(input_data)

    prediction = model.predict(X_input)[0]
    label = "spam" if prediction == 1 else "ham"
    
    return jsonify({"text": text, "prediction": label})
