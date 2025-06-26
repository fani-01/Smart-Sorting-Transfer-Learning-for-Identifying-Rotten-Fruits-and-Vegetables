from flask import Flask, render_template, request, jsonify, url_for, redirect
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from PIL import Image
import numpy as np
import os
import tensorflow as tf

app = Flask(__name__)
model = tf.keras.models.load_model('healthy_vs_rotten_keras.ipynb')
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict', methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        image = request.files['image']
        if image:
            filename = secure_filename(image.filename)
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image.save(image_path)
            model = tf.keras.models.load_model('healthy_vs_rotten.h5')
            prediction = "Tomato Rotten (Class 27)"  # Replace with actual result
            return render_template("result.html", image=filename, prediction=prediction)
    return render_template("predict.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
