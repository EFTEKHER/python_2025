import  streamlit as st
import pandas as pd
st.title("Streamlit Text input")

name=st.text_input("Enter your name")
age=st.slider("Select your age",0,100,25)
options=["python","java","c++","javascript"]
language=st.selectbox("Select your favorite programming language",options)
##submit button
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old and your favorite programming language is {language}.")
    
    
data={
    "Name":["John","Jane","Doe","Smith","Emily"],
    "Age":[28,34,29,42,23],
    "City":["New York","Los Angeles","Chicago","Houston","Phoenix"]}
df=pd.DataFrame(data)
df.to_csv("data.csv",index=False)
st.write(df)

uploaded_file=st.file_uploader("Upload a CSV file",type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)