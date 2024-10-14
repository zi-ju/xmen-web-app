'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest file for ComicPoster
'''

from unittest import TestCase
from models.comic_poster import ComicPoster


class ComicPosterTest(TestCase):
    '''
    Unittests for ComicPoster class
    '''
    def test_comic_poster_init(self):
        comic_poster = ComicPoster()
        self.assertEqual(comic_poster.poster_images_url, [])
        self.assertEqual(comic_poster.poster_name, [])
        self.assertEqual(comic_poster.poster_description, [])

    def test_find_most_recent_issue_image(self):
        comic_poster = ComicPoster()
        comic_poster.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        most_recent_image_url = comic_poster.find_most_recent_issue_image(1)
        self.assertEqual(most_recent_image_url, "image_url_b")

    def test_find_most_recent_issue_image_wrong_type(self):
        comic_poster = ComicPoster()
        comic_poster.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(TypeError):
            comic_poster.find_most_recent_issue_image("a")

    def test_find_most_recent_issue_image_out_of_range(self):
        comic_poster = ComicPoster()
        comic_poster.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        with self.assertRaises(IndexError):
            comic_poster.find_most_recent_issue_image(4)

    def test_find_most_recent_issue_name(self):
        comic_poster = ComicPoster()
        comic_poster.poster_name = ["name_a", "name_b", "name_c"]
        most_recent_name = comic_poster.find_most_recent_issue_name(1)
        self.assertEqual(most_recent_name, "name_b")

    def test_find_most_recent_issue_name_wrong_type(self):
        comic_poster = ComicPoster()
        comic_poster.poster_name = ["name_a", "name_b", "name_c"]
        with self.assertRaises(TypeError):
            comic_poster.find_most_recent_issue_name("a")

    def test_find_most_recent_issue_name_out_of_range(self):
        comic_poster = ComicPoster()
        comic_poster.poster_name = ["name_a", "name_b", "name_c"]
        with self.assertRaises(IndexError):
            comic_poster.find_most_recent_issue_name(4)

    def test_find_most_recent_description(self):
        comic_poster = ComicPoster()
        comic_poster.poster_description = ["description_a", "description_b", "description_c"]
        most_recent_description = comic_poster.find_most_recent_description(1)
        self.assertEqual(most_recent_description, "description_b")

    def test_find_most_recent_description_wrong_type(self):
        comic_poster = ComicPoster()
        comic_poster.poster_description = ["description_a", "description_b", "description_c"]
        with self.assertRaises(TypeError):
            comic_poster.find_most_recent_description("b")

    def test_find_most_recent_description_out_of_range(self):
        comic_poster = ComicPoster()
        comic_poster.poster_description = ["description_a", "description_b", "description_c"]
        with self.assertRaises(IndexError):
            comic_poster.find_most_recent_description(4)

    def test_comic_poster_str(self):
        comic_poster = ComicPoster()
        comic_poster.poster_name = ["name_a", "name_b", "name_c"]
        self.assertEqual(str(comic_poster), "This is comic posters of ['name_a', 'name_b', 'name_c']")

    def test_comic_poster_eq_true(self):
        comic_poster_one = ComicPoster()
        comic_poster_one.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        comic_poster_two = ComicPoster()
        comic_poster_two.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        self.assertEqual(comic_poster_one == comic_poster_two, True)

    def test_comic_poster_eq_false(self):
        comic_poster_one = ComicPoster()
        comic_poster_one.poster_images_url = ["image_url_a", "image_url_b", "image_url_c"]
        comic_poster_two = ComicPoster()
        comic_poster_two.poster_images_url = ["image_url_d", "image_url_b", "image_url_c"]
        self.assertEqual(comic_poster_one == comic_poster_two, False)
