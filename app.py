from flask import Flask, render_template, request, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow import expand_dims
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/uploads/'
model = pickle.load(open('model.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        new_review = request.form['komentar']
        new_review = re.sub('[^a-zA-Z]', ' ', new_review)
        new_review = new_review.lower()
        new_review = new_review.split()
        pred = model.predict(new_review)
        return render_template('index.html', prediction=pred)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
