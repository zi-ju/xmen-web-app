'''
Zi Ju
CS5001, 2023 Fall
Final Project
TeamXmen class
'''

import random


class TeamXmen:
    '''
    Represents TeamXmen with attributes and functions relevant to describe the team
    Attributes:
        deck: a short description of Team Xmen
        image: main image of Team Xmen
        members_ids: a list of members' ids in Team Xmen
    Methods:
        randomly_get_a_member: Randomly select a member from Team X-Men
    '''
    def __init__(self):
        '''
        This is class TeamXmen constructor
        Paramter: nothing
        Return: nothing
        '''
        self.deck = ""
        self.image = ""
        self.members_ids = []

    def randomly_get_a_member(self):
        '''
        Method: Randomly select a member from Team X-Men
        Parameter: self
        Return:
            random_member_id - int - the id of the selected character
        '''
        random_member_id = random.choice(self.members_ids)
        return random_member_id

    def __str__(self):
        '''
        Method: __str__
        Parameter: self
        Return:
            str - str - a brief introduction of Team X-Men
        '''
        str = f"This is Team X-Men: {self.deck}"
        return str

    def __eq__(self, other):
        '''
        Method: __eq__
        Parameter: self
        Return
            True/False -- bool -- a boolean indicating whether the two objects are the same
        '''
        if isinstance(other, TeamXmen):
            if self.deck == other.deck:
                return True
        return False
