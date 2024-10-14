'''
Zi Ju
CS5001, 2023 Fall
Final Project
ComicPoster class
'''


class ComicPoster:
    '''
    ComicPoster class
    Represents ComicPoster with attributes and functions relevant to describe the poster
    Attributes:
        poster_images_url: list of url of poster image
        poster_name: list of name of the poster
        poster_description: list of description of the poster
    Methods:
        find_most_recent_issue_image: Find most recent issue image
        find_most_recent_issue_name: Find most recent issue name
        find_most_recent_description: Find most recent issue description
    '''
    def __init__(self):
        '''
        This is class ComicPoster constructor
        Paramter: nothing
        Return: nothing
        '''
        self.poster_images_url = []
        self.poster_name = []
        self.poster_description = []

    def find_most_recent_issue_image(self, index):
        '''
        Method: Find most recent issue image
        Parameter:
            self
            index - int - the index of poster in list
        Return:
            most_recent_image_url - str - url of the most recent issue image
        Raise:
            IndexError: if index out of range
            TypeError: if index is not integer
        '''
        if index > len(self.poster_images_url):
            raise IndexError("Index out of range.")
        if not isinstance(index, int):
            raise TypeError("Index should be an integer.")
        most_recent_image_url = self.poster_images_url[index]
        return most_recent_image_url

    def find_most_recent_issue_name(self, index):
        '''
        Method: Find most recent issue name
        Parameter:
            self
            index - int - the index of poster in list
        Return:
            most_recent_name - str - name of the most recent issue
        Raise:
            IndexError: if index out of range
            TypeError: if index is not integer
        '''
        if index > len(self.poster_name):
            raise IndexError("Index out of range.")
        if not isinstance(index, int):
            raise TypeError("i should be an integer.")
        most_recent_name = self.poster_name[index]
        return most_recent_name

    def find_most_recent_description(self, index):
        '''
        Method: Find most recent issue description
        Parameter:
            self
            index - int - the index of poster in list
        Return:
            most_recent_description - str - description of the most recent issue
        Raise:
            IndexError: if index out of range
            TypeError: if index is not integer
        '''
        if index > len(self.poster_description):
            raise IndexError("Index out of range.")
        if not isinstance(index, int):
            raise TypeError("i should be an integer.")
        most_recent_description = self.poster_description[index]
        return most_recent_description

    def __str__(self):
        '''
        Method: __str__
        Parameter: self
        Return:
            str - str - a brief introduction of comic posters
        '''
        str = f"This is comic posters of {self.poster_name}"
        return str

    def __eq__(self, other):
        '''
        Method: __eq__
        Parameter: self
        Return
            True/False -- bool -- a boolean indicating whether the two objects are the same
        '''
        if isinstance(other, ComicPoster):
            if self.poster_images_url == other.poster_images_url:
                return True
        return False
