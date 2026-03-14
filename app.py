from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# load model
model = pickle.load(open("churn_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    input_features = [float(x) for x in request.form.values()]
    final_features = [np.array(input_features)]

    prediction = model.predict(final_features)

    if prediction[0] == 1:
        result = "Customer will churn"
    else:
        result = "Customer will stay"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)