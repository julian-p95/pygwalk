import streamlit as st
import pandas as pd
import io
from pygwalker.api.streamlit import init_streamlit_comm, StreamlitRenderer, PreFilter

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Application Streamlit avec PyGWalker",
    layout="wide"
)

# Titre de la page
st.title("Application Streamlit avec PyGWalker")

# Téléchargement du fichier Excel
uploaded_file = st.file_uploader("Téléchargez un fichier Excel", type=["xlsx"])

if uploaded_file:
    # Lire le fichier Excel
    df = pd.read_excel(uploaded_file)
    
    # Initialisation de la communication PyGWalker
    init_streamlit_comm()

    # Mise en cache du renderer pour optimiser les performances
    @st.cache(allow_output_mutation=True)
    def get_pyg_renderer() -> "StreamlitRenderer":
        # Charger un fichier de configuration si nécessaire
        return StreamlitRenderer(df, debug=True)

    # Obtenir le renderer
    renderer = get_pyg_renderer()

    # Ajouter des filtres pré-appliqués
    pre_filters = []
    pre_filters.append(PreFilter(
        field="season",
        op="one of",
        value=[1, 2, 3]
    ))
    renderer.set_global_pre_filters(pre_filters)

    # Sélection du mode de rendu
    mode = st.selectbox("Sélectionnez le mode de rendu", ["Explore", "Renderer"])

    if mode == "Explore":
        # Mode Explore
        renderer.render_explore()
    else:
        # Mode Renderer
        chart_index = st.number_input("Indice du graphique à afficher", min_value=0, max_value=10, value=0)
        renderer.render_pure_chart(chart_index)
