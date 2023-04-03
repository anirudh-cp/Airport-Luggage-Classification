
from flask import Flask, request, render_template
import requests
import cv2
import json
import numpy as np


app = Flask(__name__)
CLASSES = ['not permitted in flights.', 'a carry-on luggage.', 'a check-in luggage.']

@app.route("/", methods = ['GET'])
def home():
    
    return render_template('index.html')


@app.route('/', methods = ['POST'])
def classify():
    
    imagefile = request.files['imagefile']
    image_path = "./website/app/images/" + imagefile.filename
    if imagefile.filename.endswith('.jpeg') or imagefile.filename.endswith('.png') or imagefile.filename.endswith('.jpg'):
        imagefile.save(image_path)
    else:
        return render_template('index.html', image_class="not a valid image.")
        
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_expanded = np.expand_dims(image_rgb, axis=0)
        
    headers = {"content-type": "application/json"}
    data = json.dumps({"signature_name": "serving_default", "instances": image_expanded.tolist()})

    json_response = requests.post('http://localhost:8501/v1/models/saved_model:predict', data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    
    predictions = json.loads(json_response.text)['predictions']

    classOut = predictions[0]['detection_classes'][0]
    image_class = CLASSES[int(classOut-1)]
    
    return render_template('index.html', image_class=image_class)
    
    
    
    