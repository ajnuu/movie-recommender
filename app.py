import streamlit as st
from recommender import recommend,movies

st.title("🎬 Movie Recommender")
st.write("Get movie recommendations based on genres")

movie_name = st.selectbox("Select Movie",movies["title"].values)

if st.button("Recommend"):

    try:
        results = recommend(movie_name)

        st.write("Recommended Movies:")

        for movie in results:
            st.write(movie)
            st.write("---")

    except Exception as e:
        st.write(e)