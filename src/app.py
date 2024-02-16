import streamlit as st 

from data.gamelogs import get_gamelog_path_map
from bi.sidebar import display_sidebar, display_momentum


def main():
    path_map = get_gamelog_path_map()
    dataframe = display_sidebar(path_map)
        
    if not dataframe is None:

        sorted_data = dataframe .sort_values(by=["QTR", "SERIES", "PLAY #"])
        sorted_data.reset_index(drop=True, inplace=True)


        
        st.header("Hello")
        with st.expander(label="Dataset"):
                st.dataframe(sorted_data)
        
        with st.expander(label="Momentum"):
                display_momentum(sorted_data)
    return 

if __name__ == "__main__":
    main()