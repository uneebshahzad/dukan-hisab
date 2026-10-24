import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Dukan Hisab", layout="centered")
st.title("Dukan Hisab Kitab")
st.markdown("---")

if 'data' not in st.session_state:
    st.session_state.data = []

with st.form("hisab_form"):
    naam = st.text_input("Grahak Ka Naam")
    raqam = st.number_input("Raqam (Rs)", min_value=0)
    qism = st.selectbox("Qism", ["Udhar", "Jama", "Kharcha"])
    btn = st.form_submit_button("Jama Karo")
    if btn and naam:
        st.session_state.data.append({"Naam": naam, "Qism": qism, "Raqam": raqam})
        st.success("Ho gaya!")

if st.session_state.data:
    df = pd.DataFrame(st.session_state.data)
    st.dataframe(df, use_container_width=True) hu
