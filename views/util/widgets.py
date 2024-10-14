'''
Zi Ju
CS5001, 2023 Fall
Final Project
Functions to display widgets
'''

import streamlit as st


def widget_button(label: str) -> bool:
    '''
    Function: Display a button and get user input
    Parameter:
        label -- str -- a short label explaining to the user what this button is for
    Return:
        pressed - bool - True if the button is pressed, false if not
    '''
    pressed = st.button(label)
    return pressed


def widget_toggle(label: str) -> bool:
    '''
    Function: Display a toggle and get user input
    Parameter:
        label -- str -- a short label explaining to the user what this toggle is for
    Return:
        pressed - bool - True if the toggle is pressed, false if not
    '''
    pressed = st.toggle(label)
    return pressed


def search_bar(label, placeholder) -> str:
    '''
    Function: Display a search bar and get user input
    Parameter:
        label -- str -- a short label explaining to the user what this search bar is for
        placeholder -- str -- a short default placeholder telling user what to input
    Return:
        user_input - str - user input string
    '''
    user_input = st.text_input(label, placeholder=placeholder)
    return user_input


def checkbox(label, key) -> bool:
    '''
    Function: Display a checkbox and get user input
    Parameter:
        label -- str -- a short label explaining to the user what this checkbox is for
        key -- str -- use as the unique key for the widget
    Return:
        checked - bool - True if the checkbox is checked
    '''
    checked = st.checkbox(label, key=key, label_visibility="collapsed")
    return checked
