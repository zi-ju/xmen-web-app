'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest for fetch data functions
'''

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout, TooManyRedirects
import unittest
import requests_mock


class TestFetchData(unittest.TestCase):
    '''
    Unittest for fetching data functions
    '''
    # Test: fetch_xmen_data
    def test_fetch_xmen_data(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "xmen"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "xmen")

    def test_fetch_xmen_data_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_xmen_data_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_xmen_data_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_xmen_data_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_mutant_characters
    def test_fetch_mutant_characters(self):
        test_url = "https://comicvine.gamespot.com/api/origin/4030-1/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "mutant"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "mutant")

    def test_fetch_mutant_characters_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/origin/4030-1/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_mutant_characters_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/origin/4030-1/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_mutant_characters_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/origin/4030-1/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_mutant_characters_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/origin/4030-1/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_all_characters_info
    def test_fetch_all_characters_info(self):
        test_url = "https://comicvine.gamespot.com/api/characters/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "all characters"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "all characters")

    def test_fetch_all_characters_info_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/characters/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_all_characters_info_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/characters/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_all_characters_info_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/characters/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_all_characters_info_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/characters/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_character_info
    def test_fetch_character_info(self):
        test_url = "https://comicvine.gamespot.com/api/character/4005-1001/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "character"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "character")

    def test_fetch_character_info_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/character/4005-1001/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_character_info_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/character/4005-1001/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_character_info_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/character/4005-1001/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_character_info_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/character/4005-1001/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_xmen_comic_issues_id_list
    def test_fetch_xmen_comic_issues_id_list(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "comic issues"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "comic issues")

    def test_fetch_xmen_comic_issues_id_list_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_xmen_comic_issues_id_list_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_xmen_comic_issues_id_list_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_xmen_comic_issues_id_list_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/team/4060-3173/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_xmen_comic_issues_info
    def test_fetch_xmen_comic_issues_info(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "comic"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "comic")

    def test_fetch_xmen_comic_issues_info_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_xmen_comic_issues_info_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_xmen_comic_issues_info_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_xmen_comic_issues_info_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)

    # Test: fetch_single_comic_issue_info
    def test_fetch_single_comic_issue_info(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        excepted_data = {
            "results": "issue"
        }
        with requests_mock.Mocker() as m:
            m.get(test_url, json=excepted_data)
            response = requests.get(test_url)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json()['results'], "issue")

    def test_fetch_single_comic_issue_info_http_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, status_code=404)
            self.assertRaises(HTTPError)

    def test_fetch_single_comic_issue_info_connection_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=ConnectionError)
            self.assertRaises(ConnectionError)

    def test_fetch_single_comic_issue_info_timeout_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=Timeout)
            self.assertRaises(Timeout)

    def test_fetch_single_comic_issue_info_too_many_redirects_error(self):
        test_url = "https://comicvine.gamespot.com/api/issues/?api_key=c14b65c66abb98bf91646318cad959b56ef0834b&format=json"
        with requests_mock.Mocker() as m:
            m.get(test_url, exc=TooManyRedirects)
            self.assertRaises(TooManyRedirects)
