import os
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Init app
app = Flask(__name__)
model = load_model('model/skin_cancer_model.h5')

# Map class indices to labels
class_labels = ['Actinic keratoses', 'Basal cell carcinoma', 'Benign keratosis', 
                'Dermatofibroma', 'Melanoma', 'Nevus', 'Vascular lesions']

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/main')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "No file uploaded", 400

    file = request.files['image']
    if file.filename == '':
        return "No file selected", 400

    # Save uploaded file
    filepath = os.path.join('static/uploads', file.filename)  # static folder so it’s accessible
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    file.save(filepath)

    # Preprocess image
    img = load_img(filepath, target_size=(64, 64))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    index = np.argmax(prediction)
    label = class_labels[index]
    confidence = prediction[0][index] * 100

    return render_template('index.html', prediction_text=f'Prediction: {label} ({confidence:.2f}% confidence)', img_path=filepath)

if __name__ == '__main__':
    app.run(debug=True)
