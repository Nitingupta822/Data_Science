from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load model
model = pickle.load(open("Model/diabetes_model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    form_data = {}
    if request.method == "POST":
        form_data = {key: request.form.get(key) for key in [
            "pregnancies", "glucose", "bp", "skin", "insulin", "bmi", "dpf", "age"
        ]}
        features = [float(form_data[key]) for key in form_data]
        prediction = model.predict([np.array(features)])[0]
        prediction = "Diabetic" if prediction == 1 else "Not Diabetic"
    return render_template("index.html", prediction=prediction, data=form_data)

if __name__ == "__main__":
    app.run(debug=True)

