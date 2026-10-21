import pickle
from pathlib import Path

import numpy as np
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

MEAN_VALUES = np.array([
    3.602814034653465,
    10.836633663366337,
    11.344950495049504,
    0.06930693069306931,
    0.5580636138613861,
    6.279908415841584,
    69.03985148514852,
    3.746209653465346,
    9.735148514851485,
    412.34158415841586,
    18.473267326732675,
    353.39282178217826,
    12.79160891089109,
], dtype=float)

STD_VALUES = np.array([
    8.089353042197608,
    22.123204621554798,
    6.869299274474925,
    0.25397535323526055,
    0.11673021759939192,
    0.7121002606489498,
    28.223253718751014,
    2.0964578017068467,
    8.720446681476702,
    168.46374041648906,
    2.126606141487338,
    95.95026367068091,
    7.226779176292222,
], dtype=float)

with MODEL_PATH.open("rb") as model_file:
    model = pickle.load(model_file)

mean = MEAN_VALUES
std = STD_VALUES

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

    data = np.array([values], dtype=float)
    scaled_data = (data - mean) / std
    prediction = model.predict(scaled_data)[0]

    return render_template("result.html", prediction=int(prediction))


if __name__ == "__main__":
    app.run(debug=True)
