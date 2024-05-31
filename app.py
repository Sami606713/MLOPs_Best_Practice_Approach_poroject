import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.prediction_pipeline import get_data

df=pd.read_csv("data/process/test_process.csv")

st.title("House Price Prediction")
col1,col2=st.columns(2)
with col1:
    bedroom=st.selectbox("Bedroom",np.unique(df["bedrooms"].values),key='bedroom')
with col2:
    bathroom=st.selectbox("Bathroom",np.unique(df["bathrooms"].values),key="bathroom")

col1,col2=st.columns(2)
with col1:
    floor=st.selectbox("Floors",np.unique(df["floors"].values),key="floors")
with col2:
    condition=st.selectbox("condition",np.unique(df["condition"].values),key="condition")

col1,col2=st.columns(2)
with col1:
    view=st.selectbox("View",np.unique(df["view"].values),key="view")
with col2:
    yr_build=st.selectbox("yr_built",np.unique(df["yr_built"].values),key="yr_built")

col1,col2=st.columns(2)
with col1:
    yr_reno=st.selectbox("yr_renovated",np.unique(df["yr_renovated"].values),key="yr_renovated")
with col2:
    city=st.selectbox("city",np.unique(df["city"].values),key="city")

col1,col2=st.columns(2)
with col1:
    country=st.selectbox("country",np.unique(df["country"].values),key="country")
with col2:
    living_area=st.text_input("Living Area",key='living area')

col1,col2=st.columns(2)
with col1:
    sqft_lot=st.text_input("Total Area",key='total area')
with col2:
    sqft_basement=st.text_input("sqft_basement",key="basement")

dic={
    "bedrooms":bedroom,'bathrooms':bathroom,"floors":floor,"view":view,"condition":condition,
    "yr_built":yr_build,'yr_renovated':yr_reno,"city":city,"country":country,
    "sqft_basement":sqft_basement,'sqft_living':living_area,"sqft_lot":sqft_lot
}
df=pd.DataFrame(dic,index=[0])
if st.button("Predict"):
    get_data(data=df)
