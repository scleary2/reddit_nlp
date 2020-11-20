import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import pickle


st.title("NLP Demonstration")


# get_input

user_input = st.text_input("What would you like to classify?")


with open("my_model.pkl", "rb") as file:
    clf = pickle.load(file)

predictions = clf.predict([user_input])

st.write(f"The model predicts: {predictions[0]}")