from flask import Flask, render_template, request, jsonify
from tensorflow import keras
import joblib
import numpy as np
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk
from tensorflow import keras

nltk.download('wordnet')
nltk.download('punkt')
ls=WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    preprocess_text=[]
    text = re.sub('[^a-zA-Z]', ' ', text)  # Remove non-alphabetic characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    words = [ls.lemmatize(word) for word in words if word not in stop_words]
    preprocess_text.append(' '.join(words))
    one_hot_rep = [keras.preprocessing.text.one_hot(words, 10000) for words in preprocess_text] 
    padded_docs = keras.preprocessing.sequence.pad_sequences(one_hot_rep, padding='pre', maxlen=600)
    return padded_docs

print(preprocess("My name is arham khan"))
