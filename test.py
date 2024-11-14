from tensorflow import keras
import joblib
import numpy as np
import pandas as pd

preprocessor_path="artifacts/data_preprocess/text_preprocessor.pkl"
model_path="artifacts/training/trained_model.h5"


text=str(input("Enter Text"))

preprocessor=joblib.load(preprocessor_path)
model=keras.models.load_model(model_path)


text=preprocessor.fit_transform([text])
names=['Human Text',"AI generated text"]


prediction=model.predict(text)
prediction=[1 if i>0.5 else 0 for i in prediction]
print(names[prediction[0]])
