'''
Zi Ju
CS5001, 2023 Fall
Final Project
Functions for processing data
'''

import streamlit as st
from bs4 import BeautifulSoup
from models.character_gallery import CharacterGallery
from models.team_xmen import TeamXmen
from models.character import Character
from models.comic_poster import ComicPoster
from models.comic_issue import ComicIssue
from helper_functions.fetch_data import get_xmen_members_ids, get_character_issue_credits, fetch_single_comic_issue_info


def build_team_xmen() -> TeamXmen:
    '''
    Function: Create a variable "xmen" of class TeamXmen, and give it information
    Parameter: nothing
    Return:
        xmen - TeamXmen - the object of class TeamXmen
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a dictionary
    '''
    xmen_info = st.session_state["team_xmen_info"]
    if xmen_info is None:
        raise ValueError("team_xmen_info in session_state.")
    if not isinstance(xmen_info, dict):
        raise TypeError("team_xmen_info should be a dictionary")
    xmen = TeamXmen()
    xmen.deck = xmen_info["deck"]
    xmen.image = xmen_info["image"]["original_url"]
    xmen.members_ids = get_xmen_members_ids(xmen_info)
    return xmen


def build_random_member(xmen: TeamXmen) -> Character:
    '''
    Function: Randomly select an id from Team Xmen and build it a character
    Parameter:
        xmen - TeamXmen - the object of class TeamXmen
    Return:
        random_member - an object of class Character, represents the random member selected
    '''
    random_member_id = xmen.randomly_get_a_member()
    random_member = build_a_character(random_member_id)
    return random_member


def build_a_character(id: int) -> Character:
    '''
    Function: Given a character id, create a variable of class Character, and give it information
    Parameter:
        id - int - a character id
    Return:
        character - Character - an object of class Character
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a list
    '''
    character = Character()
    characters_info = st.session_state["all_characters_info"]
    if characters_info is None:
        raise ValueError("all_characters_info in session_state.")
    if not isinstance(characters_info, list):
        raise TypeError("characters_info should be a list")
    for dict in characters_info:
        if id == dict["id"]:
            character.id = dict["id"]
            character.name = dict["name"]
            character.real_name = dict["real_name"]
            character.icon_image = dict["image"]["icon_url"]
            character.small_image = dict["image"]["small_url"]
            character.deck = dict["deck"]
            character.site = dict["site_detail_url"]
            if dict["aliases"]:
                character.aliases = dict["aliases"].replace("\n", ", ")
    return character


def build_character_gallery() -> CharacterGallery:
    '''
    Function: Create a variable 'gallery' of class CharacterGallery, and give it information
    Parameter: nothing
    Return:
        gallery - CharacterGallery - the object of class CharacterGallery
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a list
    '''
    gallery = CharacterGallery()
    characters_info = st.session_state["all_characters_info"]
    characters_info = st.session_state["all_characters_info"]
    if characters_info is None:
        raise ValueError("all_characters_info in session_state.")
    if not isinstance(characters_info, list):
        raise TypeError("characters_info should be a list")
    characters_info_sorted_by_appearance = sort_characters_by_appearance(characters_info)
    image_url = []
    name = []
    for dict in characters_info_sorted_by_appearance:
        image_url.append(dict["image"]["icon_url"])
        name.append(dict["name"])
    gallery.gallery_images_url = image_url
    gallery.gallery_name = name
    return gallery


def build_comic_poster(comic_issues_info_sorted_by_date: list) -> ComicPoster:
    '''
    Function: Create a variable 'poster' of class ComicPoster, and give it information
    Parameter:
        comic_issues_info_sorted_by_date - list - a list of sorted dictionaries of comic issues info
    Return:
        poster - ComicPoster - the object of class ComicPoster
    '''
    poster = ComicPoster()
    image_url = []
    name = []
    description = []
    for dict in comic_issues_info_sorted_by_date:
        image_url.append(dict["image"]["original_url"])
        name.append(dict["name"])
        if dict["description"]:
            description_in_plain_text = convert_html_to_plain_text(dict["description"])
            description.append(description_in_plain_text)
    poster.poster_images_url = image_url
    poster.poster_name = name
    poster.poster_description = description
    return poster


def build_a_comic(id: int) -> ComicIssue:
    '''
    Function: Create a variable of class ComicIssue, and give it information,
        if the given comic issue id is not in the data stored in session state, fetch data for this issue
    Parameter:
        id - int - a comic issue id
    Return:
        comic_issue - ComicIssue - an object of class ComicIssue
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a list
    '''
    comic_issue = ComicIssue()
    comic_issues_info = st.session_state['comic_issues_info']
    if comic_issues_info is None:
        raise ValueError("comic_issues_info in session_state.")
    if not isinstance(comic_issues_info, list):
        raise TypeError("comic_issues_info should be a list")
    id_found = False
    for dict in comic_issues_info:
        if id == dict["id"]:
            id_found = True
            comic_issue.name = dict["name"]
            comic_issue.volume_name = dict["volume"]["name"]
            comic_issue.small_image = dict["image"]["small_url"]
            if dict["description"]:
                description_in_plain_text = convert_html_to_plain_text(dict["description"])
                comic_issue.description = description_in_plain_text
            comic_issue.cover_date = dict["cover_date"]
    if id_found is False:
        comic_issue_info = fetch_single_comic_issue_info(id)
        comic_issue.name = comic_issue_info[0]["name"]
        comic_issue.volume_name = comic_issue_info[0]["volume"]["name"]
        comic_issue.small_image = comic_issue_info[0]["image"]["small_url"]
        description_in_plain_text = convert_html_to_plain_text(comic_issue_info[0]["description"])
        comic_issue.description = description_in_plain_text
        comic_issue.cover_date = comic_issue_info[0]["cover_date"]
    return comic_issue


def sort_characters_by_appearance(character_info: list) -> list:
    '''
    Function: Given a list of character info dictionaries, sort it according to character issue appearances
    Parameter:
        character_info - list - a list of character info dictionaries
    Return:
        characters_info_sorted_by_appearance - list - sorted list of character info dictionaries
    '''
    characters_info_sorted_by_appearance = sorted(character_info,
                                                  key=lambda x: x["count_of_issue_appearances"],
                                                  reverse=True)
    return characters_info_sorted_by_appearance


def search_and_sort_character(user_input: str) -> list:
    '''
    Function: Call functions to search character and sort result, then generate an id list of results
    Parameter:
        user_input - str - user input string
    Return:
        sorted_search_result_id_list - list - an id list of results
    Raise Error:
        ValueError - user input is empty
    '''
    if user_input == "":
        raise ValueError("You did not enter anything.")
    search_result_character_info = search_character(user_input)
    characters_info_sorted_by_appearance = sort_characters_by_appearance(search_result_character_info)
    sorted_search_result_id_list = []
    for dict in characters_info_sorted_by_appearance:
        sorted_search_result_id_list.append(dict["id"])
    return sorted_search_result_id_list


def search_character(user_input: str) -> list:
    '''
    Function: Get user input(name, real name, aliase of a character), search for the character
    Parameter:
        user_input - str - user input string
    Return:
        search_result_character_info - list - a list of character info dictionaries
    Raise Error:
        ValueError - user input is empty
    '''
    if user_input == "":
        raise ValueError("You did not enter anything.")
    search_result_character_info = []
    characters_info = st.session_state["all_characters_info"]
    for dict in characters_info:
        aliases_list = []
        real_name = ""
        name = ""
        # Convert multiple aliases in a string into items in a list, each item is an alias
        if dict["aliases"] is not None:
            aliases_string = dict["aliases"].lower()
            aliases_string = aliases_string.replace('\r', '')
            aliases_list = aliases_string.split("\n")
        if dict["real_name"] is not None:
            real_name = dict["real_name"]
        if dict["name"] is not None:
            name = dict["name"]
        if user_input.lower() in aliases_list or\
                user_input.lower() in name.lower() or\
                user_input.lower() in real_name.lower():
            search_result_character_info.append(dict)
    return search_result_character_info


def filter_xmen_member(search_result_id_list: list) -> list:
    '''
    Function: Filter Team X-Men member from the search results by deleting id of non-members from list
    Parameter:
        search_result_id_list - list - a list of characters id after searching
    Return:
        search_result_id_list - list - filtered list of ids
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a dictionary
    '''
    xmen_info = st.session_state["team_xmen_info"]
    if xmen_info is None:
        raise ValueError("team_xmen_info in session_state.")
    if not isinstance(xmen_info, dict):
        raise TypeError("team_xmen_info should be a dictionary")
    xmen_members_ids = get_xmen_members_ids(xmen_info)
    for id in search_result_id_list:
        if id not in xmen_members_ids:
            search_result_id_list.remove(id)
    return search_result_id_list


def search_comics_with_characters_appearance(selected_characters_ids: list) -> list:
    '''
    Function: According to a list of character id, search for comics in which all these characters appear in
    Parameter:
        selected_characters_ids - list - a list of character id
    Return:
        intersection_issue_credits_list - list - a list of comic issue id, of which all these characters appear in
    '''
    # Create a dictionary and each key-value in it is "character_id": [list of issue credits of this character]
    character_comic_relation = {}
    for character_id in selected_characters_ids:
        character_issue_credits = get_character_issue_credits(character_id)
        character_comic_relation[character_id] = character_issue_credits
    # Find the intersection
    intersection_issue_credits_list = []
    intersection_issue_credits = set(intersection_issue_credits_list)
    for character_id in selected_characters_ids:
        issue_credits = character_comic_relation[character_id]
        if not intersection_issue_credits:
            intersection_issue_credits = set(issue_credits)
        else:
            intersection_issue_credits = intersection_issue_credits.intersection(issue_credits)
    intersection_issue_credits_list = list(intersection_issue_credits)
    return intersection_issue_credits_list


def sort_comics_by_date() -> list:
    '''
    Function: Sort a list of comic issues info dictionaries, according to date of comic being added to dataset
    Parameter: nothing
    Return:
        comic_issues_info_sorted_by_date - list - a sorted list of comic issues info dictionaries
    Raise Error:
        ValueError - invalid value of the object
        TypeError - the object is not a list
    '''
    comic_issues_info = st.session_state['comic_issues_info']
    if comic_issues_info is None:
        raise ValueError("comic_issues_info in session_state.")
    if not isinstance(comic_issues_info, list):
        raise TypeError("comic_issues_info should be a list")
    comic_issues_info_sorted_by_date = sorted(comic_issues_info,
                                              key=lambda x: x["date_added"],
                                              reverse=True)
    return comic_issues_info_sorted_by_date


def search_comic_issue(user_input: str) -> list:
    '''
    Function: Get user input(name of comic issue), search for the comic issue
    Parameter:
        user_input - str - user input string
    Return:
        search_result_id_list - list - a list of comic issue id
    Raise Error:
        ValueError - user input is empty
    '''
    if user_input == "":
        raise ValueError("You did not enter anything.")
    search_result_id_list = []
    comic_issues_info = st.session_state['comic_issues_info']
    if comic_issues_info is None:
        raise ValueError("comic_issues_info in session_state.")
    if not isinstance(comic_issues_info, list):
        raise TypeError("comic_issues_info should be a list")
    for dict in comic_issues_info:
        comic_issue_name = dict["name"]
        comic_volumn_name = dict["volume"]["name"]
        if comic_issue_name is not None:
            if user_input.lower() in comic_issue_name.lower() or user_input.lower() in comic_volumn_name.lower():
                search_result_id_list.append(dict["id"])
        elif user_input.lower() in comic_volumn_name.lower():
            search_result_id_list.append(dict["id"])
    return search_result_id_list


def convert_input_string_to_name_list(user_input: str) -> list:
    '''
    Function: In user input string, it contains multiple names that are separated by comma,
        this function is to split the names and and remove space before or after comma.
    Parameter:
        user_input - str - user input string
    Return:
        input_name_list - a list of names, each item of the list is a name
    '''
    input_name_list = []
    if user_input:
        # Separate inputs in a string to items in a list, and remove space at the beginning and end
        input_name_list = user_input.split(",")
        for i in range(len(input_name_list)):
            input_name_list[i] = input_name_list[i].strip()
    return input_name_list


def convert_html_to_plain_text(html_string: str) -> str:
    '''
    Function: The original description found in API is in HTML format. This function is to convert
        text in html format to plain text
    Parameter:
        html_string - str - text in html format
    Return:
        plain_text - str - converted plain text
    '''
    # Convert html to plain text with beautifulsoup
    # Source: https://www.geeksforgeeks.org/converting-html-to-text-with-beautifulsoup/
    string_for_convert = BeautifulSoup(html_string, features="html.parser")
    plain_text = string_for_convert.get_text()
    return plain_text
