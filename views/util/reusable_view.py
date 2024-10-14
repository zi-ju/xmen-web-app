'''
Zi Ju
CS5001, 2023 Fall
Final Project
Functions for displaying reusable view
'''

import streamlit as st


def display_character(character) -> None:
    '''
    Function: display image and info of a character
    Parameter:
        character - Character - an object of class Character
    Return: nothing
    '''
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(character.small_image)
    with col2:
        st.markdown(f"**{character.name}**")
        st.caption(f"Real name: {character.real_name}")
        st.caption(f"Aliases: {character.aliases}")
        st.write(character.deck)
        st.link_button("See character in Comic Vine wiki", character.site)
    st.divider()


def display_comics(comic_issue) -> None:
    '''
    Function: display image and info of a comic issue
    Parameter:
        comic_issue - ComicIssue - an object of class ComicIssue
    Return: nothing
    '''
    col1, col2 = st.columns([1, 4])
    with col1:
        if comic_issue.small_image:
            st.image(comic_issue.small_image)
        else:
            st.write("No Image")
    with col2:
        # Comic name
        if comic_issue.name is not None:
            full_name = comic_issue.get_volume_issue_full_name()
            st.markdown(f"**{full_name}**")
        else:
            st.markdown(f"**{comic_issue.volume_name}**")
        # Cover Date
        st.caption(f"Cover date: {comic_issue.cover_date}")
        # Comic description
        if comic_issue.description is not None:
            st.write(comic_issue.description)
        else:
            st.write("No desciptions.")
    st.divider()


def display_result_number(search_result_id_list: list) -> None:
    '''
    Function: display the result count
    Parameter:
        search_result_id_list - list - a list of searching results
    Return: nothing
    '''
    st.caption(f"{len(search_result_id_list)} results in total.")


def display_result_number_note(max_result: int) -> None:
    '''
    Function: display a message telling user the max number of results displayed
    Parameter:
        max_result - int - the max number of results that is going to be displayed
    Return: nothing
    '''
    st.caption(f"Only displaying the first {max_result} results.")
