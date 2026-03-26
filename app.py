from flask import Flask, request, render_template
import pickle
from utils.feature_extraction import extract_features

app = Flask(__name__)

model = pickle.load(open("model/phishing_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form["url"]
        features = [0]*30
        result = model.predict([features])[0]

        prediction = "Phishing" if result == 1 else "Safe"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", 
    port=int(os.environ.get("PORT", 10000)))