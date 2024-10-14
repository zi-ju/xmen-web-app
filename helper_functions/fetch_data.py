'''
Zi Ju
CS5001, 2023 Fall
Final Project
Functions for fetching data from API
'''

import requests
import json
import streamlit as st
from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects

COMICVINE_API_URL = "https://comicvine.gamespot.com/api"
API_KEY = "?api_key=c14b65c66abb98bf91646318cad959b56ef0834b"
HEADERS = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15"}
FORMAT_JSON = "&format=json"
XMEN_TEAM_FILTER_URL = "/team/4060-3173/"
MUTANT_FILTER_URL = "/origin/4030-1/"
CHARACTERS_URL = "/characters/"
SINGLE_CHARACTER_URL = "/character/4005-"
ISSUES_URL = "/issues/"
SPIDERMAN_ID = 1443


@st.cache_data
def fetch_xmen_data() -> dict:
    '''
    Function: Fetch Team X-MEN data from Comic Vine API and store in session state.
    Parameter: nothing
    Return: a dictionary that contains team X-MEN data.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        response = requests.get(COMICVINE_API_URL + XMEN_TEAM_FILTER_URL + API_KEY + FORMAT_JSON, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["error"] == "OK":
            xmen_info = data["results"]
        if "team_xmen_info" not in st.session_state:
            st.session_state["team_xmen_info"] = xmen_info
        return xmen_info
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


@st.cache_data
def fetch_character_data():
    '''
    Function: Call functions to get id and info of all characters that this application needs
    Parameter: nothing
    Return: nothing
    '''
    # Get character data and store in session states
    # 1. Fetch from API (it's really slow and easy to occur server error and timeout.)
    mutant_characters = fetch_mutant_characters()
    all_characters_ids = get_all_characters_ids(mutant_characters)
    all_characters_info = fetch_all_characters_info(all_characters_ids)
    if "all_characters_info" not in st.session_state:
        st.session_state["all_characters_info"] = all_characters_info
    # 2. Open file (file is fetched from API and stored for easy use)
    # with open("all_characters_info.json", 'r') as file:
    #     st.session_state["all_characters_info"] = json.load(file)


@st.cache_data
def fetch_comics_data():
    '''
    Function: Call functions to get id list of all comic issues that this application needs,
        then fetch comic issue data from Comic Vine API and store in session state.
    Parameter: nothing
    Return: nothing
    '''
    # Get comic issues data and store in session states
    # 1. Fetch from API (it's really slow and easy to occur server error and timeout.)
    comic_issues_id_list = fetch_xmen_comic_issues_id_list()
    all_comic_issues_info = fetch_xmen_comic_issues_info(comic_issues_id_list)
    if 'comic_issues_info' not in st.session_state:
        st.session_state['comic_issues_info'] = all_comic_issues_info
    # 2. Open file (file is fetched from API and stored for easy use)
    # with open('comic_issues_info.json', 'r') as file:
    #     st.session_state['comic_issues_info'] = json.load(file)


def fetch_mutant_characters() -> list:
    '''
    Function: Fetch all mutant characters basic info from Comic Vine API.
    Parameter: nothing
    Return: a list of all mutant characters, each object in the list is
        a dictionary contains a url, id, name for each character.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        response = requests.get(COMICVINE_API_URL + MUTANT_FILTER_URL + API_KEY + FORMAT_JSON, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["error"] == "OK":
            mutant_characters = data["results"]["characters"]
        return mutant_characters
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


def get_xmen_members_ids(xmen_info: dict) -> list:
    '''
    Function: Get a list of ids of all Team X-Men members
    Parameter:
        xmen_info - dict - A dictionary of all Team X-men info
    Return:
        xmen_members_ids - list - a list of ids of all Team X-Men members
    '''
    xmen_members_ids = []
    for character in xmen_info["characters"]:
        character_id = character["id"]
        xmen_members_ids.append(character_id)
    # Remove the id of Spider-Man because he is wrongly added into Team X-Man by Comic Vine
    if SPIDERMAN_ID in xmen_members_ids:
        xmen_members_ids.remove(SPIDERMAN_ID)
    return xmen_members_ids


def get_all_characters_ids(mutant_characters: list) -> list:
    '''
    Function: Get id list of all characters this app needs
        by combining Team X-men id list and mutant characters id list
    Parameter:
        mutant_characters - list - a list of mutant characters basic info, each item in list is a dictionary
    Return:
        all_characters_ids - list - a list of id of all characters,
            including mutant characters and non-mutant characters from Team X-Men
    '''
    mutants_id_list = []
    for dict in mutant_characters:
        mutants_id_list.append(dict["id"])
    xmen_info = st.session_state["team_xmen_info"]
    xmen_members_ids = get_xmen_members_ids(xmen_info)
    # Get a union of items in two lists
    # Source: https://www.geeksforgeeks.org/python-union-two-lists/
    all_characters_ids = list(set(mutants_id_list) | set(xmen_members_ids))
    return all_characters_ids


def fetch_all_characters_info(all_characters_ids: list) -> list:
    '''
    Function: Fetch all characters info from Comic Vine API, according to id list.
    Parameter:
        all_characters_ids - list - a list of all characters ids
    Return:
        all_characters_info - list - a list of all characters info, each object in the list is
            a nested dictionary contains all info of a character.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        all_characters_info = []
        # Break the long id list into chunks (100 id per chunk)
        # Source: https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
        chunk_size = 100
        for i in range(0, len(all_characters_ids), chunk_size):
            id_list_chunk = all_characters_ids[i:i+chunk_size]
            # convert each int to str
            id_str_list_chunk = list(map(str, id_list_chunk))
            # convert list to string, each id separated by "|"
            id_chunk_for_filter = '|'.join(id_str_list_chunk)
            # from API fetch data for each 100 id 
            response = requests.get(COMICVINE_API_URL + CHARACTERS_URL + API_KEY +
                                    f"&filter=id:{id_chunk_for_filter}" + FORMAT_JSON, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            if data["error"] == "OK":
                all_characters_info.extend(data["results"])
            # Below lines are how I store data in file
            # with open('all_characters_info.json', 'w') as file:
            #     json.dump(all_characters_info, file)
        return all_characters_info
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


def fetch_character_info(character_id: int) -> dict:
    '''
    Function: Fetch single character info from Comic Vine API, according to character id.
    Parameter:
        character_id - int - character id
    Return:
        character_info - dict - a dictionary which contains all detailed info of a character
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        response = requests.get(COMICVINE_API_URL + SINGLE_CHARACTER_URL +
                                str(character_id) + "/" + API_KEY + "&format=json", headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["error"] == "OK":
            character_info = data["results"]
        return character_info
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


def get_character_issue_credits(id: int) -> list:
    '''
    Function: Find the list of id of comic issues that the given character appears in
    Parameter:
        id - int - character id
    Return:
        character_issue_credits - list - list of id of comic issues that the given character appears in
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        character_issue_credits = []
        character_info = fetch_character_info(id)
        for dict in character_info["issue_credits"]:
            character_issue_credits.append(dict["id"])
        return character_issue_credits
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


@st.cache_data
def fetch_xmen_comic_issues_id_list() -> list:
    '''
    Function: Fetch all comic issues that Team X-MEN appears in from Comic Vine API.
    Parameter: nothing
    Return:
        comic_issues_id_list - list - a list of comic issue id.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        comic_issues_id_list = []
        response = requests.get(COMICVINE_API_URL + XMEN_TEAM_FILTER_URL + API_KEY + FORMAT_JSON, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["error"] == "OK":
            comic_issues_dict_list = data["results"]["issue_credits"]
            for dict in comic_issues_dict_list:
                comic_issues_id_list.append(dict["id"])
        return comic_issues_id_list
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


def fetch_xmen_comic_issues_info(comic_issues_id_list: list) -> list:
    '''
    Function: Fetch all comic issues (with Team X-MEN appears in) info from Comic Vine API.
    Parameter:
        comic_issues_id_list - list - a list of id of comic issues (with Team X-MEN appears in)
    Return:
        comic_issues_id_list - list - a list of all comic issues info, Each object in the list
            is a nested dictionary contains all info of a comic issue.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        all_comic_issues_info = []
        # Break the long id list into chunks (100 id per chunk)
        # Source: https://stackoverflow.com/questions/434287/how-to-iterate-over-a-list-in-chunks
        chunk_size = 100
        for i in range(0, len(comic_issues_id_list), chunk_size):
            comic_issues_id_list_chunk = comic_issues_id_list[i:i+chunk_size]
            # convert each int to str
            comic_issues_id_str_list_chunk = list(map(str, comic_issues_id_list_chunk))
            # convert list to string, each id separated by "|"
            comic_issues_id_chunk_for_filter = '|'.join(comic_issues_id_str_list_chunk)
            # from API fetch data for each 100 id
            response = requests.get(COMICVINE_API_URL + ISSUES_URL + API_KEY +
                                    f"&filter=id:{comic_issues_id_chunk_for_filter}" + FORMAT_JSON, headers=HEADERS)
            response.raise_for_status()
            data = response.json()
            if data["error"] == "OK":
                all_comic_issues_info.extend(data["results"])
        # Below lines are how I store data in file
        # with open('comic_issues_info.json', 'w') as file:
        #     json.dump(all_comic_issues_info, file)
        return all_comic_issues_info
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")


def fetch_single_comic_issue_info(comic_issue_id: int) -> list:
    '''
    Function: Fetch single comic issue info from Comic Vine API.
    Parameter:
        comic_issue_id - int - id of a comic issue
    Return:
        comic_issue_info - a list that contains the dictionary of comic issue info.
    Raises Error: HTTPError, ConnectionError, Timeout, TooManyRedirects
    '''
    try:
        response = requests.get(COMICVINE_API_URL + ISSUES_URL + API_KEY +
                                f"&filter=id:{comic_issue_id}" + FORMAT_JSON, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data["error"] == "OK":
            comic_issue_info = data["results"]
        return comic_issue_info
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error occurred: {http_err}. Please try again.")
    except ConnectionError as conn_err:
        raise ConnectionError(f"Connection error occurred: {conn_err}. Please try again.")
    except Timeout as timeout_err:
        raise Timeout(f"Timeout error occurred: {timeout_err}. Please try again.")
    except TooManyRedirects as redirect_err:
        raise TooManyRedirects(f"Redirect error occurred: {redirect_err}. Please try again.")
