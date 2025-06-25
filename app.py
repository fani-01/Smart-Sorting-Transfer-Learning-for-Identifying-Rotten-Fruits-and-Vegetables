import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
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
            # Here, call your model.predict(image_path) if needed
            prediction = "Tomato Rotten (Class 27)"  # Replace with actual result
            return render_template("result.html", image=filename, prediction=prediction)
    return render_template("predict.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
