'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest file for TeamXmen
'''

from unittest import TestCase
import random
from models.team_xmen import TeamXmen


class TeamXmenTest(TestCase):
    '''
    Unittests for TeamXmen class
    '''
    def test_team_xmen_init(self):
        team_xmen = TeamXmen()
        self.assertEqual(team_xmen.deck, "")
        self.assertEqual(team_xmen.image, "")
        self.assertEqual(team_xmen.members_ids, [])

    def test_randomly_get_a_member(self):
        team_xmen = TeamXmen()
        team_xmen.members_ids = [1000, 1001, 1002, 1003]
        # Use random.seed() to test method using random number
        # Source: https://www.w3schools.com/python/ref_random_seed.asp
        random.seed(1)
        random_member_id = team_xmen.randomly_get_a_member()
        self.assertEqual(random_member_id, 1001)

    def test_team_xmen_str(self):
        team_xmen = TeamXmen()
        team_xmen.deck = "abcdefg"
        self.assertEqual(str(team_xmen), "This is Team X-Men: abcdefg")

    def test_team_xmen_eq_true(self):
        team_xmen_a = TeamXmen()
        team_xmen_a.deck = "abcdefg"
        team_xmen_b = TeamXmen()
        team_xmen_b.deck = "abcdefg"
        self.assertEqual(team_xmen_a == team_xmen_b, True)

    def test_team_xmen_eq_false(self):
        team_xmen_a = TeamXmen()
        team_xmen_a.deck = "abcdefg"
        team_xmen_b = TeamXmen()
        team_xmen_b.deck = "abcd"
        self.assertEqual(team_xmen_a == team_xmen_b, False)
