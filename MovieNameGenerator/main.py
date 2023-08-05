import streamlit as st
import langchain_helper

st.title("Movie Recommendation by AI")

movie = st.sidebar.selectbox("Superman","Batman","Inception")

if movie:
    response = langchain_helper.generate_movie_name(movie)
    st.header(response['movie_name'].strip())
    menu_items = response['movies'].strip().split(",")
    st.write("**Must Watch**")
    for item in menu_items:
        st.write("-", item)

