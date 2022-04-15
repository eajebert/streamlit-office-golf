import streamlit as st

with st.sidebar:
    n_holes = int(st.number_input("No. of hole played", min_value=1))
    dropdown_options = [f"Hole {hole + 1}" for hole in range(n_holes)]
    st.selectbox("Select hole to edit:", dropdown_options)