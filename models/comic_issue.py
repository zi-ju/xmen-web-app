'''
Zi Ju
CS5001, 2023 Fall
Final Project
ComicIssue class
'''


class ComicIssue:
    '''
    ComicIssue class
    Represents ComicIssue with attributes and functions relevant to describe the comic issue
    Attributes:
        name: name of the comic issue
        wolume_name: name of the volume that this issue appears in
        small_image: small image url of this comic issue
        description: description of this comic issue
        cover_date: cover date of this comic issue (missing this info in some comic issues)
    Methods:
        get_volume_issue_full_name: get the full name (volume:issue) of this issue
    '''
    def __init__(self):
        '''
        This is class ComicIssue constructor
        Paramter: nothing
        Return: nothing
        '''
        self.name = ""
        self.volume_name = ""
        self.small_image = ""
        self.description = ""
        self.cover_date = None

    def get_volume_issue_full_name(self):
        '''
        Method: Get the full name (volume:issue) of this issue
        Parameter: self
        Return:
            volume_issue_full_name - str - full name (volume:issue) of this issue
        '''
        volume_issue_full_name = f"{self.volume_name}: {self.name}"
        return volume_issue_full_name

    def __str__(self):
        '''
        Method: __str__
        Parameter: self
        Return:
            str - str - a brief introduction of comic issue
        '''
        str = f"This is {self.get_volume_issue_full_name()}"
        return str

    def __eq__(self, other):
        '''
        Method: __eq__
        Parameter: self
        Return
            True/False -- bool -- a boolean indicating whether the two objects are the same
        '''
        if isinstance(other, ComicIssue):
            if self.get_volume_issue_full_name() == other.get_volume_issue_full_name():
                return True
        return False
