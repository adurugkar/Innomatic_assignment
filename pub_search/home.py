
import streamlit as st
import pandas as pd
import numpy as np

st.title("Welcome")
st.header("You can find the bar by local_authority")

# reaning localtion_files
#reaing columns name 
columns = pd.read_csv("data\data_dictionary - Sheet1.csv",usecols=["Field"] )
#reading dataset
df=pd.read_csv('data/open_pubs.csv', names = columns.Field)
#replacing '\N' with null value
df=df.replace('\\N',np.NaN)
#removing null value rows
df=df.dropna()

df.to_csv("data/use_full.csv", index=False)