import streamlit as st
import pandas as pd
import os

from kaggle.api.kaggle_api_extended import KaggleApi

# Kaggle API initialisieren
api = KaggleApi()
api.authenticate()

# Dataset herunterladen und laden
dataset_url = 'jainaru/world-happiness-report-2024-yearly-updated'
file_name = 'World-happiness-report-2024.csv'

@st.cache_data
def download_and_load_data(dataset_url, file_name, num_of_records):
    api.dataset_download_file(dataset_url, file_name, path='.')
    return pd.read_csv(file_name).head(num_of_records)



# Radio Buttons
visibility = st.radio("Visibility", key="visibility", options=["visible", "hidden"])

# Slider
form = st.form("my_form1")
form.slider("Inside the form",key="slider")
submitted1 = form.form_submit_button("Submit")

# Daten anzeigen
if visibility == "visible":
    st.title('World Happiness Report 2024')
    data = download_and_load_data(dataset_url, file_name, st.session_state.slider)
    st.write(data)
else:
    st.write("Nothing")

