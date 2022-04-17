import os
from flask import Flask
from flask_restful import Resource,Api,reqparse
import joblib
import numpy as np
import pandas as pd


model = joblib.load('demo.pkl')

app = Flask(__name__)
api = Api(app)

class pred(Resource):
 def __init__(self):
  self._feat = ['Time']
  self.reqparse = reqparse.RequestParser()
  for feature in self._feat:
   self.reqparse.add_argument(feature,type=int,required=True,location='json',help="no data passed")
  super(pred,self).__init__()
 
 def post(self):
  arg = self.reqparse.parse_args()
  X = np.array([arg[i] for i in self._feat]).reshape(-1,1)
  y = model.predict(X)
  return {'pred':y.tolist()[0]}
 
api.add_resource(pred,'/pred')
if __name__=='__main__':
 app.run(debug=True,host='0.0.0.0')


