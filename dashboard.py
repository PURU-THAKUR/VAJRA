import streamlit as st
import pandas as pd
from app.trainer.model import train_model
from app.utils.helpers import load_sample_data

def show_dashboard():
    st.title("⚡ Vajra Dashboard")
    run_training = st.sidebar.button("Run Model")
    df = load_sample_data()
    st.dataframe(df)
    if run_training:
        acc = train_model(df)
        st.success(f"Accuracy: {acc:.2f}")
