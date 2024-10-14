'''
Zi Ju
CS5001, 2023 Fall
Final Project
Character class
'''


class Character:
    '''
    Character class
    Represents Character with attributes and functions relevant to describe the character
    Attributes:
        id: id of the character
        url: url of the character
        name: name of the character
        deck: short description of the character
        aliases: aliases of the character
        real_name: real name of the character
        screen_large_image: url of screen large image of the character
        icon_image: url of icon image of the character
        small_image: url of small image of the character
        comic_issues: list of all comic issues that this character appears in
        site: url of the external website of the character
    Methods:
        get_name_string: get the full name (name: real name) of this character
    '''
    def __init__(self):
        '''
        This is class Character constructor
        Paramter: nothing
        Return: nothing
        '''
        self.id = None
        self.url = ""
        self.name = ""
        self.deck = ""
        self.aliases = None
        self.real_name = ""
        self.icon_image = ""
        self.small_image = ""
        self.comic_issues = []
        self.site = ""

    def get_character_full_name(self):
        '''
        Method: Get the full name (name: real name) of this character
        Parameter: self
        Return:
            full_name - str - full name (name: real name) of this character
        '''
        full_name = f"{str(self.name)} ({str(self.real_name)})"
        return full_name

    def __str__(self):
        '''
        Method: __str__
        Parameter: self
        Return:
            str - str - a brief introduction of character
        '''
        str = f"This is {self.get_character_full_name()}"
        return str

    def __eq__(self, other):
        '''
        Method: __eq__
        Parameter: self
        Return
            True/False -- bool -- a boolean indicating whether the two objects are the same
        '''
        if isinstance(other, Character):
            if self.id == other.id:
                return True
        return False
