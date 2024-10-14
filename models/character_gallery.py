'''
Zi Ju
CS5001, 2023 Fall
Final Project
CharacterGallery class
'''


class CharacterGallery:
    '''
    CharacterGallery class
    Represents CharacterGallery with attributes and functions relevant to describe the character gallery
    Attributes:
        gallery_images_url: list of image urls in this gallery
        gallery_name: list of image names in this gallery
    Methods:
        get_image_for_each: find the image url by index
        get_name_for_each: find the image name by index
    '''
    def __init__(self):
        '''
        This is class CharacterGallery constructor
        Paramter: nothing
        Return: nothing
        '''
        self.gallery_images_url = []
        self.gallery_name = []

    def get_image_for_each_character(self, index):
        '''
        Method: find the image url by index
        Parameter:
            self
            index - int - the index of image in list
        Return:
            image - str - url of the image
        Raise:
            IndexError: if i out of range
            TypeError: if i is not integer
        '''
        if index > len(self.gallery_images_url):
            raise IndexError("Index out of range.")
        if not isinstance(index, int):
            raise TypeError("Index should be an integer.")
        image = self.gallery_images_url[index]
        return image

    def get_name_for_each_character(self, index):
        '''
        Method: find the image name by index
        Parameter:
            self
            index - int - the index of image name in list
        Return:
            image - str - name of the image
        Raise:
            IndexError: if index out of range
            TypeError: if index is not integer
        '''
        if index > len(self.gallery_images_url):
            raise IndexError("Index out of range.")
        if not isinstance(index, int):
            raise TypeError("Index should be an integer.")
        name = self.gallery_name[index]
        return name

    def __str__(self):
        '''
        Method: __str__
        Parameter: self
        Return:
            str - str - a brief introduction of character gallery
        '''
        str = f"This is character gallery of {self.gallery_name}"
        return str

    def __eq__(self, other):
        '''
        Method: __eq__
        Parameter: self
        Return
            True/False -- bool -- a boolean indicating whether the two objects are the same
        '''
        if isinstance(other, CharacterGallery):
            if self.gallery_images_url == other.gallery_images_url:
                return True
        return False
