import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import numpy as np

st.write("""
# Max of 3 numbers App
This app gives maximum among 3 input numbers.

""")

st.header('Enter 3 numbers')

def user_input_features():
    
    number_1 = st.number_input("first number")
    number_2 = st.number_input("second number")
    number_3 = st.number_input("third number")

    data = {'first number': number_1,
            'second number': number_2,
            'third number': number_3
    }

    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

list = []

if st.button('Get Maximum'):
    
        
        list = [df['first number'].values.tolist()[0], 
                df['second number'].values.tolist()[0],
                df['third number'].values.tolist()[0]]


st.header('Maximum :')
if list != []:
        st.write(max(list))
