import streamlit as st
import pandas as pd
import joblib
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# Preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from scipy.stats import f_oneway

# Model
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

# Evaluation metrics
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Load model
model = joblib.load(r'C:\Users\Salman\Data science\You_tube_ad_projrct\ad_revenue_model.pkl')

st.title("YouTube Ad Revenue Predictor")

# Inputs
views = st.text_input("Views")
likes = st.text_input("Likes")
comments = st.text_input("Comments")
watch_time = st.text_input("Watch Time (minutes)")
video_length = st.text_input("Video Length (minutes)")
subscribers = st.text_input("Subscribers")

category = st.selectbox("Category", ['Select', 'Entertainment', 'Gaming', 'Education', 'Music', 'Tech','Lifestyle'])
if category == 'Select':
    category = np.nan
device = st.selectbox("Device", ['Select','TV', 'Tablet', 'Mobile', 'Desktop'])
if device == 'Select':
    device = np.nan
country = st.selectbox("Country", ['Select','IN', 'CA', 'UK', 'US', 'DE', 'AU'])
if country == 'Select':
    country = np.nan

# function to change the data type to numeric or null value
def to_numeric_or_nan(value):
    return pd.to_numeric(value, errors='coerce') if value != "" else np.nan

views = to_numeric_or_nan(views)
likes = to_numeric_or_nan(likes)
comments = to_numeric_or_nan(comments)
watch_time = to_numeric_or_nan(watch_time)
video_length = to_numeric_or_nan(video_length)
subscribers = to_numeric_or_nan(subscribers)


# Predict button
if st.button("Predict Revenue"):
    
    input_df = pd.DataFrame({
        'views': [views],
        'likes': [likes],
        'comments': [comments],
        'watch_time_minutes': [watch_time],
        'video_length_minutes': [video_length],
        'subscribers': [subscribers],
        'category': [category],
        'device': [device],
        'country': [country]
    })
    
    prediction = model.predict(input_df)
    
    st.success(f"Estimated Ad Revenue: ${prediction[0][0]:.2f}")

st.subheader('Insights')

st.text('The below DataFrame represents the change in Ad revenue (USD) per unit increase in the that particular features keeping all other features constant.')

coef_df_num = pd.DataFrame({
    'Features' : ['Likes','Comments','Views','Watch time in minutes','video length in minutes','subscribers'],
    'Change in Ad_revenue' : ['+ 0.017 USD','+ 0.017 USD','+ 0.0066 USD','+ 0.0047 USD','+ 0.0031 USD','+ 9.11e-08 USD']
})

st.dataframe(coef_df_num)

st.text("The below DataFrame represents the change in Ad revenue (USD) of the particular type of video category compared to the 'Education video' keeping all other features constant.")

coef_df_cat = pd.DataFrame({
    'Type of video category' : ['Tech','Lifestyle','Entertainment','Music','Gaming'],
    'Change in Ad_revenue' : ['+ 0.053 USD','+ 0.018 USD','- 0.023 USD','- 0.092 USD','- 0.101 USD']
})

st.dataframe(coef_df_cat)

st.text("The below DataFrame represents the change in Ad revenue (USD) of the particular type of device compared to the 'Desktop' keeping all other features constant.")

coef_df_dev = pd.DataFrame({
    'Type of Device' : ['Mobile','Tablet','TV'],
    'Change in Ad_revenue' : ['- 0.063 USD','- 0.087 USD','- 0.235 USD']
})

st.dataframe(coef_df_dev)

st.text("The below DataFrame represents the change in Ad revenue (USD) of the particular country compared to 'Australia' keeping all other features constant.")

coef_df_con = pd.DataFrame({
    'Country' : ['India','Canada','United Kingdom','United States','Germany'],
    'Change in Ad_revenue' : ['+ 0.038 USD','- 0.031 USD','- 0.075 USD','- 0.093 USD','- 0.132 USD']
})

st.dataframe(coef_df_con)