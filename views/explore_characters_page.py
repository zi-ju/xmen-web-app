'''
Zi Ju
CS5001, 2023 Fall
Final Project
Function for displaying explore characters page
'''

import streamlit as st
from views.util.widgets import search_bar

GALLERY_COLUMN_NUMBER = 6
GALLERY_ROW_NUMBER = 3


def display_explore_characters_page():
    '''
    Function: Display Explore Characters page header
    Parameter: nothing
    Return: nothing
    '''
    st.header("Explore characters")
    st.subheader("Gallery")
    st.write("Meet the most popular characters, including Team X-Men and other Mutants!")


def display_gallery(gallery):
    '''
    Function: Display the character gallery
    Parameter:
        gallery - CharacterGallery - object of class CharacterGallery
    Return: nothing
    '''
    columns = st.columns(GALLERY_COLUMN_NUMBER)
    for i in range(GALLERY_COLUMN_NUMBER * GALLERY_ROW_NUMBER):
        with columns[i % GALLERY_COLUMN_NUMBER]:
            name = gallery.get_name_for_each_character(i)
            st.image(gallery.get_image_for_each_character(i), caption=name)


def display_character_search_bar():
    '''
    Function: Display a character search bar
    Parameter: nothing
    Return:
        user_input - str - user input string
    '''
    st.subheader("Looking for someone?")
    user_input = search_bar("Type in a character's name to search, or whatever you'd like to call him/her!",
                            "Example: Wolverine (or Logan)")
    return user_input
