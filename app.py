'''
Zi Ju
CS5001, 2023 Fall
Final Project
Driver file for X-Men app
'''

import streamlit as st
from helper_functions.fetch_data import fetch_xmen_data, fetch_character_data, fetch_comics_data
from helper_functions.process_data import (build_team_xmen, build_character_gallery, build_a_character,
                                           build_comic_poster, build_a_comic, build_random_member,
                                           filter_xmen_member, sort_comics_by_date,
                                           search_comic_issue, search_comics_with_characters_appearance,
                                           convert_input_string_to_name_list, search_and_sort_character)
from views.home_page import display_home_page, display_team_xmen, display_member
from views.explore_characters_page import (display_explore_characters_page, display_gallery, display_character_search_bar)
from views.explore_comics_page import display_explore_comics_page, display_next_poster, display_comics_search_bar
from views.find_your_characters_page import (display_find_your_characters_page, display_multi_characters_search_bar,
                                             display_selection_area, display_selection_for_each_input,
                                             display_character_and_checkbox, display_selection_result,
                                             display_comic_result_area, display_no_result)
from views.util.reusable_view import (display_character, display_comics, display_result_number, display_result_number_note)
from views.util.widgets import widget_button, widget_toggle
from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects


MAX_RESULTS_DISPLAY = 20
DEFAULT_INDEX = 0


def random_select_and_display_member(xmen) -> None:
    '''
    Function: Create an object representing a random member from Team X-Men, and display
    Parameter:
        xmen - TeamXmen - the object of class TeamXmen
    Return: nothing
    '''
    random_member = build_random_member(xmen)
    display_member(random_member)


def display_character_search_result(search_result_id_list: list) -> None:
    '''
    Function: Display result count, create object for each character in result and display
    Parameter:
        search_result_id_list - list - a list of character ids
    Return: nothing
    '''
    display_result_number(search_result_id_list)
    for id in search_result_id_list:
        character = build_a_character(id)
        display_character(character)


def display_comic_poster(poster) -> None:
    '''
    Function: display a comic poster, and set a button to show the next poster
    Parameter:
        poster - ComicPoster - an object of class ComicPoster
    Return: nothing
    '''
    # Display the most recent comic poster, and a button to display next
    # Source: https://discuss.streamlit.io/t/display-images-one-by-one-with-a-next-button/21976/3
    if "poster_index" not in st.session_state:
        st.session_state["poster_index"] = DEFAULT_INDEX
    st.button("Show next", on_click=display_next_poster(poster, st.session_state["poster_index"]))


def display_comics_search_result(comic_search_result_id_list: list, max_results_number: int) -> None:
    '''
    Function: display search result count and note. Only keep the max number of results and display each
    Parameter:
        comic_search_result_id_list - list - a list of comic issue ids
        max_results_number - int - the max number of results that is going to be displayed
    Return: nothing
    '''
    display_result_number(comic_search_result_id_list)
    display_result_number_note(max_results_number)
    displayed_comic_list = comic_search_result_id_list[:max_results_number]
    for id in displayed_comic_list:
        comic_issue = build_a_comic(id)
        display_comics(comic_issue)


def show_options_and_get_user_selection(input_name_list: list) -> list:
    '''
    Function: for each name that user searches for, call function to search for characters,
        and for each searching result, display all character options, and let user select from them using checkbox
    Parameter:
        input_name_list - list - a list in which each item is a name that user inputs
    Return:
        selected_characters_ids - list - a list of selected characters' ids
        selected_characters - str - a list of selected characters' names
    '''
    selected_characters_ids = []
    selected_characters = []
    for name in input_name_list:
        display_selection_for_each_input(name)
        search_result_id_list = search_and_sort_character(name)
        for id in search_result_id_list:
            character = build_a_character(id)
            selected = display_character_and_checkbox(character)
            if selected:
                selected_characters_ids.append(id)
                selected_characters.append(character.get_character_full_name())
    return selected_characters_ids, selected_characters


def main():
    '''
    Main function for this application
    Parameter: nothing
    Return: nothing
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects, TypeError, ValueError, KeyError, IndexError
    '''
    try:
        # Get data
        # Since the API works really slow when fetching data (it is sure that the slowness is because of the API itself),
        #   and the project needs all character and comics data to do sorting first in order to work on display features,
        #   the programmer chooses to fetch data first and store them in session state for further use,
        #   in order to make sure that after the data are all fetched, the application runs smoothly
        # Also, due to the instability of API itself, and the dataset is huge, sometimes HTTP error, server error, timeout error
        #   shows when fetching data. Please just try again if such error occurs. The fetching process has been tested to work well.
        fetch_xmen_data()
        fetch_character_data()
        fetch_comics_data()

        with st.sidebar:
            navigation_options = ["Home", "Explore characters", "Explore comics", "Find your characters"]
            selected_navigation = st.selectbox("Select page", navigation_options)

        if selected_navigation == "Home":
            xmen = build_team_xmen()
            display_home_page()
            display_team_xmen(xmen)
            st.button("Show me another!", on_click=random_select_and_display_member(xmen))

        if selected_navigation == "Explore characters":
            with st.sidebar:
                user_input = display_character_search_bar()
                xmen_member_filtered = widget_toggle("Only show Team X-Men member")
                search_button_pressed = widget_button("Search")
            if not search_button_pressed:
                gallery = build_character_gallery()
                display_explore_characters_page()
                display_gallery(gallery)
            else:
                search_result_id_list = []
                if user_input:
                    search_result_id_list = search_and_sort_character(user_input)
                if xmen_member_filtered:
                    search_result_id_list = filter_xmen_member(search_result_id_list)
                display_character_search_result(search_result_id_list)

        if selected_navigation == "Explore comics":
            with st.sidebar:
                user_input = display_comics_search_bar()
                search_button_pressed = widget_button("Search")
            comic_search_result_id_list = []
            if not search_button_pressed:
                display_explore_comics_page()
                comic_issues_info_sorted_by_date = sort_comics_by_date()
                poster = build_comic_poster(comic_issues_info_sorted_by_date)
                display_comic_poster(poster)
            else:
                comic_search_result_id_list = []
                if user_input:
                    comic_search_result_id_list = search_comic_issue(user_input)
                    display_comics_search_result(comic_search_result_id_list, MAX_RESULTS_DISPLAY)

        if selected_navigation == "Find your characters":
            display_find_your_characters_page()
            user_input = display_multi_characters_search_bar()
            searched = widget_button("Search")
            input_name_list = convert_input_string_to_name_list(user_input)
            if user_input:
                with st.form("select"):
                    display_selection_area()
                    selected_characters_ids, selected_characters = show_options_and_get_user_selection(input_name_list)
                    selection_submitted = st.form_submit_button("Select")
                if selection_submitted:
                    display_comic_result_area()
                    display_selection_result(selected_characters)
                    intersection_issue_credits_list = search_comics_with_characters_appearance(selected_characters_ids)
                    if intersection_issue_credits_list:
                        display_comics_search_result(intersection_issue_credits_list, MAX_RESULTS_DISPLAY)
                    else:
                        display_no_result()

    except IndexError as ex:
        st.write("Error: ", type(ex), ex)
    except TypeError as ex:
        st.write("Error: ", type(ex), ex)
    except ValueError as ex:
        st.write("Error: ", type(ex), ex)
    except KeyError as ex:
        st.write("Error: ", type(ex), ex)
    except HTTPError as ex:
        st.write("Error: ", type(ex), ex)
    except ConnectionError as ex:
        st.write("Error: ", type(ex), ex)
    except Timeout as ex:
        st.write("Error: ", type(ex), ex)
    except TooManyRedirects as ex:
        st.write("Error: ", type(ex), ex)


if __name__ == "__main__":
    main()
