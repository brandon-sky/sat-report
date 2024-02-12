import os

import pandas as pd
import streamlit as st 

import bi.elements as business_analytics


def main():
    dataframe = business_analytics.display_sidebar()
    
    st.header("Hello")
    with st.expander(label="Dataset"):
        if not dataframe is None:
            st.dataframe(dataframe)
    return 

if __name__ == "__main__":
    main()