"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st

# Data handling dependencies
import pandas as pd
import numpy as np

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
def main():

    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System","Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))

        # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                           top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                              We'll need to fix it!")


    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------
    if page_selection == "Solution Overview":
        st.title("Solution Overview")
        st.write("For our solution we decided to merge multiple dataframes together and try to create models based on the genre columns.")
	st.image('resources/imgs/merge.png',use_column_width=True)
	st.image('resources/imgs/movies_genres.png',use_column_width=True)
	st.write("We tried a number of models but eventualy settled for an optimized SVD model which scored us an RMSE of 0.79 on Kaggle")
	st.image('resources/imgs/kaggle.png',use_column_width=True)

    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.
	
   if page_selection == "Exploratory Data Analysis":
	st.title("Exploratory Data Analysis")
        st.write("We were given access to a number of csv files which contained data relating to movies. The csv files were transformed into dataframes as follows:")
	st.write("sample_submission.csv - this was just an example of the layout for how our submission to Kaggle should be formatted")
	st.image('resources/imgs/df_sample_submission.png',use_column_width=True)
	st.write("movies.csv - this was a csv containing movie ids, movie titles as well as a list of genres that a movie belonged to")
	st.image('resources/imgs/df_movies.png',use_column_width=True)
	st.write("imdb_data.csv - this file contained information pertaining to movies sourced from imdb")
	st.image('resources/imgs/df_imdb.png',use_column_width=True)
	st.write("genome_scores.csv - this file contained information pertaining to movies with relevance")
	st.image('resources/imgs/df_genome_scores.png',use_column_width=True)
	st.write("genome_tags.csv - this file contained information pertaining to movies and contained timestamps and tags")
	st.image('resources/imgs/df_tags.png',use_column_width=True)
	st.write("train.csv - this file contained information on movie titles, user ids and their respective ratings")
	st.image('resources/imgs/df_train.png',use_column_width=True)
	st.write("test.csv - this file contained information on movie titles and user ids without ratings")
	st.image('resources/imgs/df_test.png',use_column_width=True)
	st.write("tags.csv - this file contained information on movie titles and user ids as well as associated tags")
	st.image('resources/imgs/df_tags.png',use_column_width=True)
	st.write("links.csv - this file contained ids for use with linking the various dataframes together")
	st.image('resources/imgs/df_links.png',use_column_width=True)
	st.write("We had a look into the most common genre of movies:")
	st.image('resources/imgs/genres.png',use_column_width=True)
	st.write("Since the dataset was so large we also subseted the data to contain only movies that had at least 50 ratings:")
	st.image('resources/imgs/min_ratings.png',use_column_width=True)
	st.write("We also created a visualizaton to detemine the number of ratings as well as the actual ratings. It may be noted that people tend to rate slighly higher than lower")
	st.image('resources/imgs/number_ratings.png',use_column_width=True) ##if issue...
	st.write("We also had a look of movie titles by popularity:")
	st.image('resources/imgs/pop_titles.png',use_column_width=True)
	st.write("And did a further investigation based on the nubmer of movies released per director:")
	st.image('resources/imgs/director_movies.png',use_column_width=True)
	st.write("We also investigated the number of ratings each director have recieved:")
	st.image('resources/imgs/director_ratings.png',use_column_width=True)
	

if __name__ == '__main__':
    main()
