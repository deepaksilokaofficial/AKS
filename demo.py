import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv('data.csv')
print(df)

model = LinearRegression().fit(df['Time'].to_numpy().reshape(-1,1),df['Marks'].to_numpy().reshape(-1,1))
pred = model.predict(df['Time'].to_numpy().reshape(-1,1))
print(pred)

joblib.dump(value=model,filename='demo.pkl')
