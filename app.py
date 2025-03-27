import streamlit as st
import requests

st.set_page_config(page_title="Traduction", page_icon="💬")

def main():
    st.title("Traduction de fichiers")

    fichier = st.file_uploader("Choisissez un fichier", type=["txt"])
    texte_origine = ""

    # Lecture éventuelle du fichier (sans conditionner l'affichage des zones de texte)
    if fichier is not None:
        st.write("Nom du fichier :", fichier.name)
        content = fichier.read()
        if content is not None:
            texte_origine = content.decode("utf-8")

    # Box de lecture du fichier avant la sélection de la langue
    st.text_area("Aperçu du fichier :", value=texte_origine, height=200)

    # Récupération de la liste de langues depuis l'API /languages
    try:
        response = requests.get("http://localhost:5000/languages")
        if response.status_code == 200:
            languages = response.json()
        else:
            languages = ["Français", "Anglais", "Espagnol", "Autre"]
    except:
        languages = ["Français", "Anglais", "Espagnol", "Autre"]

    langue_sortie = st.selectbox("Langue de sortie :", languages)

    # Bouton de traduction affiché sans condition
    if st.button("Traduire"):
        st.session_state["translated_text"] = ""
        st.write(f"Traduction en {langue_sortie} en cours...")

    # Zones de texte affichées en permanence
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