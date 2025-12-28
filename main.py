import streamlit as st
from app.ui.dashboard import show_dashboard

def main():
    st.set_page_config(page_title="Vajra Dashboard", layout="wide")
    show_dashboard()

if __name__ == "__main__":
    main()
