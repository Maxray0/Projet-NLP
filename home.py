import streamlit as st

st.set_page_config(page_title="Accueil", page_icon="🏠", layout="centered")

def main():
    st.title("Page d'accueil")
    st.markdown(
        """<h3 style='text-align:center; color:#09e3eb;'>
        Bienvenue ! Sélectionnez une page :
        </h3>""",
        unsafe_allow_html=True
    )
    st.markdown(
        """<a href="/traduction" target="_self" style="font-size:1.2rem;">
        ▶ Traduction
        </a>""",
        unsafe_allow_html=True
    )

if __name__ == "__main__":  
    main()