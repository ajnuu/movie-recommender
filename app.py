import streamlit as st
from recommender import recommend

st.title("🎬 Movie Recommender")

movie = st.text_input("Enter Movie Name")

if st.button("Recommend"):

    try:
        results = recommend(movie)

        st.write("Recommended Movies:")

        for r in results:
            st.write(r)

    except:
        st.write("Movie not found")