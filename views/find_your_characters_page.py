'''
Zi Ju
CS5001, 2023 Fall
Final Project
Function for displaying explore comics page
'''

import streamlit as st
from views.util.reusable_view import display_character
from views.util.widgets import search_bar, checkbox


def display_find_your_characters_page():
    '''
    Function: Display Find Your Characters page header
    Parameter: nothing
    Return: nothing
    '''
    st.header("Find your characters")


def display_multi_characters_search_bar():
    '''
    Function: Display a search bar for entering one or multiple character names, and get user input
    Parameter: nothing
    Return:
        user_input - str - user input string
    '''
    st.subheader("Type in any character you want!")
    user_input = search_bar("Type in one or more characters' name, \
                            or whatever you'd like to call them! Separate by comma (', ')",
                            "Example: Scott Summers, Jean Grey")
    return user_input


def display_selection_area():
    '''
    Function: Display subheader of selection area
    Parameter: nothing
    Return: nothing
    '''
    st.subheader("Here to select your character")


def display_selection_for_each_input(name):
    '''
    Function: Display the guideline for selecting each character
    Parameter:
        name - str - each name that user inputs
    Return: nothing
    '''
    st.write("Select your character: ", name)


def display_character_and_checkbox(character):
    '''
    Function: Display a checkbox for selecting character, and info of character
    Parameter:
        character - Character - object of class Character
    Return:
        selected - bool - True if the character is selected
    '''
    col1, col2 = st.columns([1, 20])
    with col1:
        selected = checkbox(str(character.id), str(character.id))
    with col2:
        display_character(character)
    return selected


def display_selection_result(selected_characters: list):
    '''
    Function: Display a message showing the selection result
    Parameter:
        selected_characters - list - a list of selected characters' names
    Return:
        selected - bool - True if the character is selected
    '''
    selected_characters_string = ", ".join(selected_characters)
    st.write("You selected: ", selected_characters_string)


def display_comic_result_area():
    '''
    Function: Display subheader of result area
    Parameter: nothing
    Return: nothing
    '''
    st.subheader("See your results")


def display_no_result():
    '''
    Function: Display a message if no results found
    Parameter: nothing
    Return: nothing
    '''
    st.write("They haven't appeared in same issues.")
