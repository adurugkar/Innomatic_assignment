# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
import numpy as np
import app

# reaning localtion_files
data = pd.read_csv(r"C:\Users\avina\Desktop\innomatic_assignment\Innomatic_assignment\Streamlit\my_app\data\use_full.csv")
total_local_authority = set(data.local_authority)
st.write("Search nearest BAR")

#to find nearest latitude and longitude
def nearest_pub(n1,n2):
    data = pd.read_csv(r"C:\Users\avina\Desktop\innomatic_assignment\Innomatic_assignment\Streamlit\my_app\data\use_full.csv")
    data1 = data.longitude.astype('float')
    data2 = data.latitude.astype('float')
    res = pd.DataFrame(zip(data1, data2))
    test = np.array([n1,n2])
    distances=np.sqrt(np.sum(np.sqrt(res-test),axis=1))
    idx=np.argsort(distances)
    res = data.iloc[idx[:5]]    
    return res
     
number1 = st.number_input('Insert your current latitude')
number2 = st.number_input("insert your curren longitude")
button = st.button(f"Search BAR")

if button:
    
    st.write(f"insert latitude is {number1} and inster longitude is {number2}")
    res = nearest_pub(number1, number2)
    
    
    st.map(res)
