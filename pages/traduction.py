import streamlit as st
import requests
import PyPDF2
from io import BytesIO

st.set_page_config(page_title="Traduction", page_icon="💬")

def main():
    st.title("Traduction de fichiers (PDF uniquement)")

    # Autoriser uniquement PDF côté Streamlit
    fichier = st.file_uploader("Choisissez un fichier PDF", type=["pdf"])
    texte_origine = ""

    if fichier is not None:
        # Extraction du texte depuis .pdf
        lecteur_pdf = PyPDF2.PdfReader(fichier)
        for page in lecteur_pdf.pages:
            texte_origine += page.extract_text() or ""

    st.text_area("Aperçu du fichier :", value=texte_origine, height=200)

    # Récupération de la liste de langues depuis l'API /languages
    try:
        response = requests.get("http://localhost:8000/languages")
        if response.status_code == 200:
            languages = response.json()
        else:
            languages = {"Français": "fra_Latn", "Anglais": "eng_Latn"}
    except:
        languages = {"Français": "fra_Latn", "Anglais": "eng_Latn"}

    # Afficher la liste de langues
    langue_sortie = st.selectbox("Langue de sortie :", list(languages.keys()))

    if st.button("Traduire"):
        if not texte_origine.strip():
            st.warning("Aucun texte détecté.")
        else:
            st.session_state["translated_text"] = ""

            # Préparation du paramètre target_lang pour l'API
            cible_nllb = languages.get(langue_sortie, "eng_Latn")

            # Conversion du PDF en fichier in-memory
            fichier.seek(0)  # Réinitialiser le pointeur
            files = {"file": (fichier.name, fichier.read(), "application/pdf")}
            params = {"target_lang": cible_nllb}

            response = requests.post("http://localhost:8000/traduction", files=files, params=params)

            if response.status_code == 200:
                result = response.json()
                st.write(f"Langue détectée : {result.get('detected_language', 'inconnue')}")
                st.session_state["translated_text"] = result.get("translated_text", "")
            else:
                st.write("Erreur lors de la traduction.")

    col1, col2 = st.columns(2)
    with col1:
        st.text_area("Texte d'origine", value=texte_origine, height=200)
    with col2:
        if "translated_text" not in st.session_state:
            st.session_state["translated_text"] = ""
        st.session_state["translated_text"] = st.text_area(
            "Texte traduit",
            value=st.session_state["translated_text"],
            height=200
        )

if __name__ == "__main__":
    main()