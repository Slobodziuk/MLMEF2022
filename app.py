import numpy as np
from flask import Flask, request, render_template
import pickle
from pathlib import Path

app = Flask(__name__)
model = pickle.load(open('./pressurePredictionCopenhagen-Model.pkl','rb'))


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    #Get required number of input fields from the HTML page
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    return render_template(
        "index.html", Pressure_prediction="Likely pressure is: {}".format([prediction[0]])
    )

if __name__ == "__main__":
    app.run(debug=True)
