from tensorflow import keras
import joblib
import numpy as np
import pandas as pd

preprocessor_path="artifacts/data_preprocess/text_preprocessor.pkl"
model_path="artifacts/training/trained_model.h5"
data="artifacts/data_clean/data_clean.csv"

df=pd.read_csv(data)
X=df['text']
Y=df['generated']

preprocessor=joblib.load(preprocessor_path)
model=keras.models.load_model(model_path)


text=preprocessor.fit_transform(X)

prediction=model.predict(text)
prediction=[1 if i>0.5 else 0 for i in prediction]
