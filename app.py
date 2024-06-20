import streamlit as st
import pickle

movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movies_list=movies['title'].values

st.header('Movie Recommendation System')
selectvalue=st.selectbox("Select Movie from dropdown", movies_list)

def recommend(movies):
    index=movies[movies['title']==movies].index[0]
    distance=sorted(list(enumerate(similarity[index])), reverse= True, key=lambda vector:vector[1])
    recommend_movie=[]
    for i in distance[0:5]:
        recommend_movie.append(movies.iloc[i[0]].title)
    return recommend_movie



if st.button('Show Recommend'):
    movies_name=recommend(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movies_name[0])
    with col2:
        st.text(movies_name[1])
    with col3:
        st.text(movies_name[2])
    with col4:
        st.text(movies_name[3])
    with col5:
        st.text(movies_name[4])