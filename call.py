import requests
import json
import cv2
import numpy as np
import pandas as pd

IMAGE_PATHS = './Dataset/Train/2.jpg'
class_names = ['Not permitted', 'Carry on', 'Check in']


# Works for './Dataset/Train/25.jpg' (check), './Dataset/Train/5.jpeg' (carry), './Dataset/Train/2.jpg' (carry), './Dataset/Test/1.jpg' (not)


image = cv2.imread(IMAGE_PATHS)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_expanded = np.expand_dims(image_rgb, axis=0)


data = json.dumps({"signature_name": "serving_default", "instances": image_expanded.tolist()})
print('Data: {} ... {}'.format(data[:50], data[len(data)-52:]))


headers = {"content-type": "application/json"}
json_response = requests.post('http://localhost:8501/v1/models/saved_model:predict', data=data, headers=headers)
predictions = json.loads(json_response.text)['predictions']

classOut = predictions[0]['detection_classes'][0]

print(f'The predicted class is {class_names[int(classOut-1)]} (id={classOut})')