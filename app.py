from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/hdi_model.pkl")


@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    category = None

    if request.method == "POST":

        life = float(request.form["life"])
        expected = float(request.form["expected"])
        mean = float(request.form["mean"])
        gni = float(request.form["gni"])

        import pandas as pd

        input_data = pd.DataFrame([{
                 "Life": life,
                 "Expected": expected,
                  "Mean": mean,
              "GNI": gni
              }])

        result = model.predict(input_data)[0]

        # Keep prediction between 0 and 1
        prediction = max(0.0, min(round(result, 3), 1.0))

        if prediction >= 0.800:
            category = "Very High Human Development"
        elif prediction >= 0.700:
            category = "High Human Development"
        elif prediction >= 0.550:
            category = "Medium Human Development"
        else:
            category = "Low Human Development"

    return render_template(
        "index.html",
        prediction=prediction,
        category=category
    )


if __name__ == "__main__":
    app.run(debug=True)