import streamlit as st
import time
import pandas as pd
import requests
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from PIL import Image;

#titl = Image.open('./title.png')
img = Image.open('icon.jpg')

final = pd.read_csv('final.csv')
url = pd.read_csv('url.csv')

st.set_page_config(page_title='Book Recommender',
                   #page_icon=img,
                   layout="centered",
                   initial_sidebar_state="collapsed",
                   menu_items={
                       'Get Help': None,
                       'Report a bug': None,
                       'About': "# Created with :heart: by *Shubham Pandkar*!"
                   }
                   )
st.image(img,use_column_width=None)
def create_matrix(df):
    N = len(df['User-ID'].unique())
    M = len(df['Book-ID'].unique())

    # Map IDs to indices
    user_mapper = dict(zip(np.unique(df["User-ID"]), list(range(N))))
    book_mapper = dict(zip(np.unique(df["Book-ID"]), list(range(M))))

    # Map indices to IDs
    user_inv_mapper = dict(zip(list(range(N)), np.unique(df["User-ID"])))
    book_inv_mapper = dict(zip(list(range(M)), np.unique(df["Book-ID"])))

    user_index = [user_mapper[i] for i in df['User-ID']]
    book_index = [book_mapper[i] for i in df['Book-ID']]

    X = csr_matrix((df["Book-ID"], (book_index, user_index)), shape=(M, N))

    return X, user_mapper, book_mapper, user_inv_mapper, book_inv_mapper

X, user_mapper, book_mapper, user_inv_mapper, book_inv_mapper = create_matrix(final)



#st.image(titl, use_column_width=None)


#def fetch_poster(book_id):
#    response = requests.get(
#        'https://api.themoviedb.org/3/movie/{}?api_key=REPLACE-YOUR-API-KEY&language=en-US'.format(movie_id))
#    data = response.json()
#    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(book_id, X, k, metric='cosine', show_distance=False):
    neighbour_ids = []
    poster_url = []
    titles = []
    book_ind = book_mapper[book_id]
    book_vec = X[book_ind]
    k += 1
    kNN = NearestNeighbors(n_neighbors=k, algorithm="brute", metric=metric)
    kNN.fit(X)
    book_vec = book_vec.reshape(1, -1)
    neighbour = kNN.kneighbors(book_vec, return_distance=show_distance)
    for i in range(0, k):
        n = neighbour.item(i)
        neighbour_ids.append(book_inv_mapper[n])
    neighbour_ids.pop(0)
    book_titles = dict(zip(final['Book-ID'], final['Book-Title']))
    url_dict = dict(zip(url['Book-ID'], url['Image-URL-M']))
    for i in neighbour_ids:
        titles.append(book_titles[i])
    for i in neighbour_ids:
        poster_url.append(url_dict[i])

    return titles, poster_url


st.header('Book Recommendation System')
title_values = final['Book-Title'].unique()
selected_book_name = st.selectbox(
    'Enter Book Name',
    title_values)

if st.button('Recommend '):
    book_ids = final.loc[final['Book-Title']==selected_book_name,'Book-ID'].iloc[0]
    book_id = int(book_ids)
    names, posters = recommend(book_id,X, k=10)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    col5, col6, col7, col8 = st.columns(4)
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])

    col9, col10 = st.columns(2)
    with col9:
        st.text(names[8])
        st.image(posters[8])
    with col10:
        st.text(names[9])
        st.image(posters[9])
    #with st.spinner('Wait for it...'):
    #    time.sleep(0)
#st.snow()




