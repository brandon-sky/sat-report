import os

import pandas as pd
import streamlit as st 

from data.gamelogs import get_gamelog_path_map
from bi.sidebar import display_sidebar


def main():
    path_map = get_gamelog_path_map()
    dataframe = display_sidebar(path_map)
    
    st.header("Hello")
    with st.expander(label="Dataset"):
        if not dataframe is None:
            st.dataframe(dataframe)
    return 

if __name__ == "__main__":
    main()