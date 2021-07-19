import streamlit as st
import pandas as pd


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_training = st.beta_container()

with header:
    st.title("Welcome to Movie Recommendations!")
    st.text("In this project we look into the Recommendations of the Movies")


with dataset:
    st.header("Movie Recommendations")
    st.text("This dataset was found from EDSA")

        movie_data = pd.read_csv("")
        st.write(movie_data.head())




with features:
    st.header("The features I created")



with model_training:
    st.header("Time to train the model")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance change")