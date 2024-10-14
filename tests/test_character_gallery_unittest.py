'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest file for CharacterGallery
'''

from unittest import TestCase
from models.character_gallery import CharacterGallery


class CharacterGalleryTest(TestCase):
    '''
    Unittests for CharacterGallery class
    '''
    def test_comic_poster_init(self):
        gallery = CharacterGallery()
        self.assertEqual(gallery.gallery_images_url, [])
        self.assertEqual(gallery.gallery_name, [])

    def test_get_image_for_each_character(self):
        gallery = CharacterGallery()
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        image = gallery.get_image_for_each_character(1)
        self.assertEqual(image, "image_url_b")

    def test_get_image_for_each_character_wrong_type(self):
        gallery = CharacterGallery()
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(TypeError):
            gallery.get_image_for_each_character("a")

    def test_get_image_for_each_character_out_of_range(self):
        gallery = CharacterGallery()
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(IndexError):
            gallery.get_image_for_each_character(4)

    def test_get_name_for_each_character(self):
        gallery = CharacterGallery()
        gallery.gallery_name = ["name_a", "name_b", "name_c"]
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        name = gallery.get_name_for_each_character(2)
        self.assertEqual(name, "name_c")

    def test_get_name_for_each_character_wrong_type(self):
        gallery = CharacterGallery()
        gallery.gallery_name = ["name_a", "name_b", "name_c"]
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(TypeError):
            gallery.get_name_for_each_character("a")

    def test_get_name_for_each_character_out_of_range(self):
        gallery = CharacterGallery()
        gallery.gallery_name = ["name_a", "name_b", "name_c"]
        gallery.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(IndexError):
            gallery.get_image_for_each_character(4)

    def test_character_gallery_str(self):
        gallery = CharacterGallery()
        gallery.gallery_name = ["name_a", "name_b", "name_c"]
        self.assertEqual(str(gallery), "This is character gallery of ['name_a', 'name_b', 'name_c']")

    def test_character_gallery_eq_true(self):
        gallery_one = CharacterGallery()
        gallery_one.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        gallery_two = CharacterGallery()
        gallery_two.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        self.assertEqual(gallery_one == gallery_two, True)

    def test_character_gallery_eq_false(self):
        gallery_one = CharacterGallery()
        gallery_one.gallery_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        gallery_two = CharacterGallery()
        gallery_two.gallery_images_url = ["image_url_d", "image_url_b", "image_url_c"]
        self.assertEqual(gallery_one == gallery_two, False)
