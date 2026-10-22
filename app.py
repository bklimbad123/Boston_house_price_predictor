import pickle
from pathlib import Path

import pandas as pd
from flask import Flask, render_template, request

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "final_model.pickle"

FEATURES = [
    "Crime Rate",
    "Zone",
    "Industries",
    "Charles River",
    "Nitric Oxide Conc.",
    "Rooms",
    "Age",
    "Distance",
    "Highways",
    "Tax",
    "Teacher Ratio",
    "African-American",
    "Lower Status",
]

with MODEL_PATH.open("rb") as model_file:
    pipeline_artifacts = pickle.load(model_file)

model = pipeline_artifacts["model"]
imputer = pipeline_artifacts["imputer"]
scaler = pipeline_artifacts["scaler"]

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    values = []
    for field in FEATURES:
        value = request.form.get(field)
        if value is None:
            return render_template("index.html")
        values.append(float(value))

    data = pd.DataFrame([values], columns=imputer.feature_names_in_)
    imputed_data = imputer.transform(data)
    scaled_data = scaler.transform(imputed_data)
    prediction = model.predict(scaled_data)[0]

    return render_template("result.html", prediction=int(prediction))


if __name__ == "__main__":
    app.run(debug=True)
