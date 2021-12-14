#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import request as request_f
from flask import jsonify
from urllib import request
from PIL import Image
import os
from io import BytesIO

import pickle
import numpy as np
from tensorflow import keras

model_file = 'traffic-sign-model.h5'
model = keras.models.load_model(model_file)

categories = [
  'ahead_only',
  'beware_of_icesnow',
  'bicycles_crossing',
  'bumpy_road',
  'children_crossing',
  'dangerous_curve_to_the_left',
  'dangerous_curve_to_the_right',
  'double_curve',
  'end_of_all_speed_and_passing_limits',
  'end_of_no_passing',
  'end_of_no_passing_by_vehicles_over_3.5_metric_tons',
  'end_of_speed_limit_80kmh',
  'general_caution',
  'go_straight_or_left',
  'go_straight_or_right',
  'keep_left',
  'keep_right',
  'no_entry',
  'no_passing',
  'no_passing_for_vehicles_over_3.5_metric_tons',
  'no_vehicles',
  'pedestrians',
  'priority_road',
  'right-of-way_at_the_next_intersection',
  'road_narrows_on_the_right',
  'road_work',
  'roundabout_mandatory',
  'slippery_road',
  'speed_limit_100kmh',
  'speed_limit_120kmh',
  'speed_limit_20kmh',
  'speed_limit_30kmh',
  'speed_limit_50kmh',
  'speed_limit_60kmh',
  'speed_limit_70kmh',
  'speed_limit_80kmh',
  'stop',
  'traffic_signals',
  'turn_left_ahead',
  'turn_right_ahead',
  'vehicles_over_3.5_metric_tons_prohibited',
  'wild_animals_crossing',
  'yield'
]

def load_img_from_url(url):
    print(url)
    with request.urlopen(url) as url:
        f = BytesIO(url.read())

    img = Image.open(f)
    return img

def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

def prepare_input(x):
    return x / 255.0

def predict(url):
  img = load_img_from_url(url)
  img = prepare_image(img, target_size=(32, 32))

  x = np.array(img)
  X = np.array([x])
  X = prepare_input(X)

  preds = model.predict(X).round(4)

  float_predictions = preds[0].tolist()

  return dict(zip(categories, float_predictions))

app = Flask('classification')

@app.route('/heartbit', methods=['GET'])
def heartbit():
    return 'ok'

@app.route('/classification', methods=['POST'])
def classification():
    data = request_f.get_json()
    result = predict(data['url'])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
