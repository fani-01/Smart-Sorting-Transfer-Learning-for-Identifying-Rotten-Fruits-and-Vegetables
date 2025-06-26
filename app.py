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

@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        f = request.files['pc_image']
        upload_path = os.path.join('static/uploads', f.filename)
        f.save(upload_path)

        img = load_img(upload_path, target_size=(224, 224))
        img_array = img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        prediction_index = np.argmax(model.predict(img_array), axis=1)[0]
        prediction_label = index[prediction_index]

        return render_template("portfolio-details.html", predict=prediction_label)


@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
