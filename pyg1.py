import streamlit as st
import pandas as pd
import pygwalker as pyg
import streamlit.components.v1 as components

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Utilisation de PyGWalker dans Streamlit avec to_html",
    layout="wide"
)

# Titre de la page
st.title("Utilisation de PyGWalker dans Streamlit avec to_html")

# Charger les données d'exemple
df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")

# Génération du HTML avec PyGWalker
pyg_html = pyg.to_html(df)

# Intégration du HTML dans l'application Streamlit
components.html(pyg_html, height=1000, scrolling=True)
