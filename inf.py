import joblib
import os
import numpy as np

MODEL_DATA = os.environ.get('MODEL_DATA')

def pred(MODEL_DATA):
 temp = list(MODEL_DATA)
 temp = list(map(int,MODEL_DATA.split(',')))
 data = np.array(temp).reshape(-1,1)
 model = joblib.load('demo.pkl')
 pre = model.predict(data)
 return list(pre)

print(pred(MODEL_DATA)) 

