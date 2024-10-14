'''
Zi Ju
CS5001, 2023 Fall
Final Project
Unittest file for ComicIssue
'''

from unittest import TestCase
from models.comic_issue import ComicIssue


class ComicIssueTest(TestCase):
    '''
    Unittests for ComicIssue class
    '''
    def test_comic_issue_init(self):
        comic_issue = ComicIssue()
        self.assertEqual(comic_issue.name, "")
        self.assertEqual(comic_issue.volume_name, "")
        self.assertEqual(comic_issue.small_image, "")
        self.assertEqual(comic_issue.description, "")
        self.assertEqual(comic_issue.cover_date, None)

    def test_get_volume_issue_full_name(self):
        comic_issue = ComicIssue()
        comic_issue.name = "Book"
        comic_issue.volume_name = "Box"
        volume_issue_full_name = comic_issue.get_volume_issue_full_name()
        self.assertEqual(volume_issue_full_name, "Box: Book")

    def test_comic_issue_str(self):
        comic_issue = ComicIssue()
        comic_issue.name = "Book"
        comic_issue.volume_name = "Box"
        self.assertEqual(str(comic_issue), "This is Box: Book")

    def test_comic_issue_eq_true(self):
        comic_issue_a = ComicIssue()
        comic_issue_a.name = "Book"
        comic_issue_a.volume_name = "Box"
        comic_issue_b = ComicIssue()
        comic_issue_b.name = "Book"
        comic_issue_b.volume_name = "Box"
        self.assertEqual(comic_issue_a == comic_issue_b, True)

    def test_comic_issue_eq_false(self):
        comic_issue_a = ComicIssue()
        comic_issue_a.name = "Book"
        comic_issue_a.volume_name = "Box"
        comic_issue_b = ComicIssue()
        comic_issue_b.name = "Page"
        comic_issue_b.volume_name = "Box"
        self.assertEqual(comic_issue_a == comic_issue_b, False)
