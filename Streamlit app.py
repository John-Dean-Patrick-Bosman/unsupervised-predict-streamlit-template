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

        movie_data = pd.read_csv("movies.csv")
        st.write(movie_data.head())




with features:
    st.header("The features I created")



with model_training:
    st.header("Time to train the model")
    st.text("Here you get to choose the hyperparameters of the model and see how the performance change")

    Recommander.py

    # User-based preferences
    st.write('### Enter Your Three Favorite Movies')
        # movie_1 = st.selectbox('Fisrt Option',title_list[1493:1520])
        # movie_2 = st.selectbox('Second Option',title_list[2110:2120])
        # movie_3 = st.selectbox('Third Option',title_list[4110:4120])
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            try:
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = content_model(movie_list=fav_movies,
                                                        top_n=10)
            except:
                st.error("Oops! Looks like this algorithm does't work.\
                          We'll need to fix it!")
            if st.button("Recommend"):
                   st.title("We think you'll like:")
                   for i,j in enumerate(top_recommendations):
                       st.subheader(str(i+1)+'. '+j)
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
            try:
                with st.spinner('Crunching the numbers...'):
                    top_recommendations = collab_model(movie_list=fav_movies,
                                                       top_n=10)
            except:
                st.error("Oops! Looks like this algorithm does't work.\
                          We'll need to fix it!")
            if st.button("Recommend"):
                st.title("We think you'll like:")
                for i,j in enumerate(top_recommendations):
                    st.subheader(str(i+1)+'. '+j)
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

def pred_movies(movie_list):
    # Return a list of user id's
    return id_store

def collab_model(movie_list,top_n=10):
    """Performs Collaborative filtering based upon a list of movies supplied
       by the app user.

def collab_model(movie_list,top_n=10):
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n + 1]:
    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies_df['title'])[i])
    return recommended_movies

def data_preprocessing(subset_size):
    movies_subset = movies[:subset_size]
    return movies_subset

def content_model(movie_list,top_n=10):
    """Performs Content filtering based upon a list of movies supplied
       by the app user.

def content_model(movie_list,top_n=10):
    top_50_indexes = list(listings.iloc[1:50].index)
    # Removing chosen movies
    top_indexes = np.setdiff1d(top_50_indexes,[idx_1,idx_2,idx_3])
    for i in top_indexes[:top_n + 1]:
    for i in top_indexes[:top_n]:
        recommended_movies.append(list(movies['title'])[i])
    return recommended_movies