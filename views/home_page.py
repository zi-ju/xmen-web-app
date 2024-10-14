'''
Zi Ju
CS5001, 2023 Fall
Final Project
Function for displaying home page
'''

import streamlit as st


def display_home_page():
    '''
    Function: Display home page header
    Parameter: nothing
    Return: nothing
    '''
    st.header("Welcome to the world of X-MEN!")


def display_team_xmen(xmen):
    '''
    Function: Display the main image and introduction of Team Xmen
    Parameter:
        xmen - TeamXmen - object of class TeamXmen
    Return: nothing
    '''
    st.image(xmen.image)
    st.write(xmen.deck)


def display_member(random_member):
    '''
    Function: Display the image name and introduction of the random member
    Parameter:
        random_member - Character - object of class Character
    Return: nothing
    '''
    st.subheader("See a member!")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.image(random_member.small_image)
    with col2:
        st.write(f"**{random_member.name}**")
        st.write(random_member.deck)
