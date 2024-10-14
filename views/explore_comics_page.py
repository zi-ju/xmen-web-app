'''
Zi Ju
CS5001, 2023 Fall
Final Project
Function for displaying explore comics page
'''

import streamlit as st
from views.util.widgets import search_bar


def display_explore_comics_page():
    '''
    Function: Display Explore Comics page header
    Parameter: nothing
    Return: nothing
    '''
    st.header("Explore comics and movies")
    st.subheader("Haven't read the most recent comics? See what our X-MEN have been up to lately!")


def display_next_poster(poster, i: int):
    '''
    Function: Use session state to store the poster index and display poster
    Parameter:
        poseter - ComicPoster - object of class ComicPoster, in which multiple posters are stored
        i - int - index of poster
    Return: nothing
    '''
    display_comic_poster(poster, i)
    st.session_state["poster_index"] += 1
    if st.session_state["poster_index"] >= len(poster.poster_images_url):
        st.session_state["poster_index"] = 0


def display_comic_poster(poster, i: int):
    '''
    Function: Display the comic poster, title and introduction
    Parameter:
        poseter - ComicPoster - object of class ComicPoster, in which multiple posters are stored
        i - int - index of poster
    Return: nothing
    '''
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image(poster.find_most_recent_issue_image(i))
    with col2:
        st.markdown(f"**{poster.find_most_recent_issue_name(i)}**")
        st.caption(poster.find_most_recent_description(i))


def display_comics_search_bar():
    '''
    Function: Display a comic issue search bar
    Parameter: nothing
    Return:
        user_input - str - user input string
    '''
    st.subheader("Looking for any comics?")
    user_input = search_bar("Type in the name of a comic", "Example: Uncanny X-Men")
    return user_input
