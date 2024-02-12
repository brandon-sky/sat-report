import pandas as pd
import streamlit as st

def _read_hudl_export(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def display_sidebar(games: dict) -> str:
    with st.sidebar:
        selection = st.selectbox(label="Games", options=games.keys())

        if st.button("Load Dataset"):
            return _read_hudl_export(games.get(selection))