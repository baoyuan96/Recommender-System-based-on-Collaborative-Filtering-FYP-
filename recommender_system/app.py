import pickle
import streamlit as st
import pandas as pd
import requests

def recommend(hotel):
    hotel_index = hotels[hotels['Property_Name'] == hotel].index[0]
    distances = similarity[hotel_index]
    hotels_list = sorted(list(enumerate(similarity[hotel_index])),reverse=True,key = lambda x: x[1])
    
    recommended_hotels = []
    for i in hotels_list[1:6]:
        recommended_hotels.append(hotels.iloc[i[0]].Property_Name)
    return recommended_hotels

hotels_dict = pickle.load(open('hotel_dict.pkl','rb'))
hotels = pd.DataFrame(hotels_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.header('Hotel Recommender System')

selected_hotel = st.selectbox(
    "Type or select a hotel from the dropdown",
    hotels['Property_Name'].values)

if st.button('Show Recommendation'):
    recommendations = recommend(selected_hotel)
    for i in recommendations:
        st.write(i)