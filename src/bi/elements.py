import pandas as pd
import streamlit as st

import service.gamelogs as service

def _read_hudl_export(path: str) -> pd.DataFrame:
    return pd.read_excel(path)

def display_sidebar() -> str:
    games_map = service.get_games_map()

    with st.sidebar:
        selection = st.selectbox(label="Games", options=games_map.keys())

        if st.button("Load Dataset"):
            return _read_hudl_export(games_map.get(selection))