import streamlit as st

# Configuration de la page
st.set_page_config(page_title="Analyse de CV", page_icon="📄")

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
# Imports des fonctions métier (à adapter selon votre implémentation)
try:
    from your_cv_module import extract_text, extract_skills, extract_experiences, score_match
except ImportError:
    # Placeholders si le module n'existe pas encore
    def extract_text(file):
        return ""
    def extract_skills(text):
        return []
    def extract_experiences(text):
        return []
    def score_match(text, job_desc):
        return 0.0

# Titre
st.title("📄 Analyse de CV")

# Upload du CV
uploaded_file = st.file_uploader(
    "Uploadez un CV (PDF, DOCX, PNG, JPG)",
    type=["pdf", "docx", "png", "jpg"]
)

if uploaded_file:
    # Extraction de texte
    with st.spinner("Extraction du texte en cours..."):
        texte = extract_text(uploaded_file)
    st.subheader("Texte extrait")
    st.text_area("", texte, height=200)

    # Extraction des compétences
    st.subheader("Compétences détectées")
    skills = extract_skills(texte)
    if skills:
        st.write(skills)
    else:
        st.info("Aucune compétence détectée.")

    # Extraction des expériences
    st.subheader("Expériences")
    experiences = extract_experiences(texte)
    if experiences:
        for exp in experiences:
            st.markdown(f"- **{exp.get('title', '')}**: {exp.get('duration', '')}")
    else:
        st.info("Aucune expérience détectée.")

    # Scoring de compatibilité
    st.subheader("Matching avec une fiche de poste")
    job_desc = st.text_area("Entrez la description de la fiche de poste", height=100)
    if job_desc and st.button("Calculer compatibilité"):
        score = score_match(texte, job_desc)
        st.metric(label="Score de compatibilité", value=f"{score:.2f}")
    
else:
    st.info("Veuillez uploader un CV pour commencer l'analyse.")
