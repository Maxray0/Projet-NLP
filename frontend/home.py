# pages/1_🏠_Accueil.py
import streamlit as st

# Configure la page
st.set_page_config(page_title="Accueil", page_icon="🏠", layout="wide")
st.markdown("""
    <style>
        [data-testid="stSidebarNavSeparator"] {
            display: none !important;
        }
        /* Cacher le menu natif auto-généré par Streamlit dans la sidebar */
        [data-testid="stSidebarNavItems"] {
            display: none !important;
        }
        [data-testid="stSidebarNav"] {
            margin-top: -40px;  /* Optionnel : ajustement vertical */
        }
        footer, #MainMenu, header {
            visibility: hidden;
        }
    </style>
""", unsafe_allow_html=True)
# Barre de navigation personnalisée dans le sidebar
with st.sidebar:
    st.title("🧭 Navigation")
    st.page_link("home.py", label="🏠 Accueil")
    st.page_link("pages/traduction.py", label="💬 Traduction")
    st.page_link("pages/analyse_cv.py", label="📄 Analyse CV")
    st.page_link("pages/mood.py", label="📝 Analyse de sentiment")
    st.page_link("pages/analyse_docs.py", label="🗂 Docs Admin.")

# Contenu de la page Accueil
st.title("🏠 Bienvenue sur Projet-NLP")
st.markdown(
    """
    Bienvenue sur la plateforme **Projet-NLP** !

    Cette application propose trois cas d’usage principaux :
    - 💬 **Traduction** : Traduction de documents OCRisés.
    - 📄 **Analyse de CV** : Extraction de compétences, expériences et scoring de profils.
    - 🗂 **Docs Admin.** : Classification, extraction d’informations clés et résumé de documents administratifs.

    Sélectionnez un module dans la barre latérale pour démarrer.
    """
)


