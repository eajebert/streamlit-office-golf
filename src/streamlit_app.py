import streamlit as st

with st.sidebar:
    n_holes = int(st.number_input("No. of hole played", min_value=1))
    format_hole = lambda x: f"Hole {x}"
    st.selectbox("Select hole to edit:", range(1, n_holes+1), format_func=format_hole)

# It's a variable that doesn't exist.
# st.number_of_shots