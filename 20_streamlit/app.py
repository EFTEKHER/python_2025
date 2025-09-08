import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


## Title of the application
st.title("My First Streamlit App")
st.subheader("Exploring Streamlit for Data Science and Machine Learning")

## display a simple text
st.write("My name is Eftekher Ali Efte")

## create a simple dataframe
data = {
    'A': [1,2,3,4,5],
    'B': [2,3,4,5,6],
    'C': [3,4,5,6,7]
}
df = pd.DataFrame(data)

## write dataframe to the app
st.write("Here is a simple dataframe:")
st.dataframe(df)

## create a simple line chart
char_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(char_data)