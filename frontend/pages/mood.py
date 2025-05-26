import streamlit as st
import PyPDF2
from transformers import pipeline
from io import BytesIO

# Configuration de la page
st.set_page_config(page_title="Analyse de sentiment", page_icon="📝")

# Masquer la navigation native
st.markdown(
    """
    <style>
    ul[data-testid="stSidebarNavItems"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True
)

# Barre de navigation personnalisée
with st.sidebar:
    st.title("🧭 Navigation")
    st.page_link("home.py", label="🏠 Accueil")
    st.page_link("pages/traduction.py", label="💬 Traduction")
    st.page_link("pages/analyse_cv.py", label="📄 Analyse CV")
    st.page_link("pages/mood.py", label="📝 Analyse de sentiment")
    st.page_link("pages/analyse_docs.py", label="🗂 Docs Admin.")

st.title("📝 Analyse de sentiment")

# Upload PDF
uploaded_file = st.file_uploader("Uploadez un fichier PDF", type=["pdf"])
extracted_text = ""

if uploaded_file:
    # Extraction du texte depuis le PDF
    reader = PyPDF2.PdfReader(uploaded_file)
    for page in reader.pages:
        extracted_text += page.extract_text() or ""

# Zone de texte éditable
text_to_analyze = st.text_area("Texte à analyser :", value=extracted_text, height=200)

if st.button("Analyser le sentiment"):
    if not text_to_analyze.strip():
        st.warning("Aucun texte à analyser.")
    else:
        with st.spinner("Analyse en cours..."):
            results = sentiment_analyzer(text_to_analyze)
        # Affichage des résultats
        if results and len(results) > 0:
            result = results[0]
            st.metric(label="Label détecté", value=result["label"])
            st.metric(label="Score", value=f"{result['score']:.2f}")
        else:
            st.info("Aucun résultat renvoyé par le modèle.")