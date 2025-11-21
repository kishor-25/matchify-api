from flask import Flask, request, jsonify
import joblib
import os
app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "model")
model = joblib.load(os.path.join(MODEL_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(MODEL_DIR, "vectorizer.pkl"))
@app.route("/")
def home():
    return {"message": "Matchify Resume Screening API is running!"}
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    if "resume_text" not in data:
        return jsonify({"error": "Missing resume_text"}), 400
    resume_text = data["resume_text"]
    X = vectorizer.transform([resume_text])
    prediction = model.predict(X)[0]
    return jsonify({"predicted_job_role": prediction})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
