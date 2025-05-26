cd "$(dirname "$0")" || exit 1
pip install -r requirements.txt 
streamlit run home.py 