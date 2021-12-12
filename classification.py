#!/usr/bin/env python
# coding: utf-8

import numpy as np
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor('xception', target_size=(32, 32))

from flask import Flask
from flask import request
from flask import jsonify

interpreter = tflite.Interpreter(model_path='traffic-sign-model.tflite')
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = [
  'speed_limit_70kmh',
  'speed_limit_100kmh',
  'slippery_road',
  'yield',
  'end_of_no_passing',
  'wild_animals_crossing',
  'keep_right',
  'no_passing_for_vehicles_over_3.5_metric_tons',
  'speed_limit_50kmh',
  'turn_right_ahead',
  'speed_limit_30kmh',
  'go_straight_or_right',
  'turn_left_ahead',
  'vehicles_over_3.5_metric_tons_prohibited',
  'end_of_speed_limit_80kmh',
  'children_crossing',
  'right-of-way_at_the_next_intersection',
  'keep_left',
  'end_of_no_passing_by_vehicles_over_3.5_metric_tons',
  'ahead_only',
  'general_caution',
  'double_curve',
  'no_passing',
  'road_work',
  'no_vehicles',
  'dangerous_curve_to_the_left',
  'road_narrows_on_the_right',
  'bumpy_road',
  'go_straight_or_left',
  'beware_of_icesnow',
  'speed_limit_80kmh',
  'speed_limit_20kmh',
  'speed_limit_60kmh',
  'traffic_signals',
  'dangerous_curve_to_the_right',
  'end_of_all_speed_and_passing_limits',
  'speed_limit_120kmh',
  'stop',
  'roundabout_mandatory',
  'priority_road',
  'pedestrians',
  'no_entry',
  'bicycles_crossing'
]

def predict(url):
  X = preprocessor.from_url(url)

  interpreter.set_tensor(input_index, X)
  interpreter.invoke()
  preds = interpreter.get_tensor(output_index)

  float_predictions = preds[0].tolist()

  return dict(zip(classes, float_predictions))

app = Flask('classification')

@app.route('/heartbit', methods=['GET'])
def heartbit():
    return 'ok'

@app.route('/classification', methods=['POST'])
def classification():
    data = request.get_json()
    print('data', data)
    result = predict(data['url'])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
