from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow import expand_dims
import numpy as np
import os
import pickle

app = Flask(__name__)
model_file = open("model.pkl", "rb")
model = pickle.load(model_file, encoding="bytes")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_review = request.form["komentar"]
        new_review = new_review.lower()
        new_review = new_review.split()
        array_new_review = [new_review]
        print(array_new_review)
        pred = (model.predict(array_new_review))[0]
        print(pred)
        return render_template("index.html", prediction=pred)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
