'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest file for Character
'''

from unittest import TestCase
from models.character import Character


class CharacterTest(TestCase):
    '''
    Unittests for Character class
    '''
    def test_character_init(self):
        character = Character()
        self.assertEqual(character.id, None)
        self.assertEqual(character.url, "")
        self.assertEqual(character.name, "")
        self.assertEqual(character.deck, "")
        self.assertEqual(character.aliases, None)
        self.assertEqual(character.real_name, "")
        self.assertEqual(character.icon_image, "")
        self.assertEqual(character.small_image, "")
        self.assertEqual(character.comic_issues, [])
        self.assertEqual(character.site, "")

    def test_get_character_full_name(self):
        character = Character()
        character.name = "Cyclops"
        character.real_name = "Scott Summers"
        full_name = character.get_character_full_name()
        self.assertEqual(full_name, "Cyclops (Scott Summers)")

    def test_character_str(self):
        character = Character()
        character.name = "Cyclops"
        character.real_name = "Scott Summers"
        self.assertEqual(str(character), "This is Cyclops (Scott Summers)")

    def test_character_eq_true(self):
        character_a = Character()
        character_a.id = 1000
        character_b = Character()
        character_b.id = 1000
        self.assertEqual(character_a == character_b, True)

    def test_character_eq_false(self):
        character_a = Character()
        character_a.id = 1000
        character_b = Character()
        character_b.id = 1001
        self.assertEqual(character_a == character_b, False)
