import streamlit as st 

import service.gamelogs as service
import bi.elements as bi
from data.gamelogs import get_gamelog_path_map


def main():
    path_map = get_gamelog_path_map()
    dataframe = bi.display_sidebar(path_map)
    if not dataframe is None:
        sorted_data = dataframe.sort_values(by=["QTR", "SERIES", "PLAY #"]).copy()
        sorted_data.reset_index(drop=True, inplace=True)
        sorted_data['YARD LN'].ffill(inplace=True) 
        sorted_data['QTR'].ffill(inplace=True) 
        sorted_data = sorted_data.astype({"YARD LN": int})
        sorted_data["UNIFIED_YARDS"] = sorted_data["YARD LN"].apply(service.unified_view_yard_ln)        
        sorted_data["xP"] = sorted_data["UNIFIED_YARDS"].apply(service.expected_point_value)

        with st.expander(label="Dataset"):
                st.dataframe(sorted_data)
        
        with st.expander(label="Momentum"):
                bi.display_momentum(sorted_data)
        
        with st.expander(label="Expected Points"):
                bi.display_xp(sorted_data)
    return 

if __name__ == "__main__":
    main()