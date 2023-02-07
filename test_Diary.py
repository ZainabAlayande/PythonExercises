from unittest import TestCase

from DiaryApp.Diary import Diary_App
from DiaryApp.Entry import Entry_App

my_diary = Diary_App("zainab", "1234", False)


class TestDiary_App(TestCase):

    def setUp(self):
        Diary_App("zainab", "1234", False)

    def test_count_of_entry(self):
        my_diary.create_entry("Life", "Is a mystery")
        my_diary.create_entry("Love", "is sacrifice")
        my_diary.create_entry("Friendship", "is the sweetest", )
        result = my_diary.get_count_of_entry_created()
        self.assertEquals(3, result)

    def test_delete_entry(self):
        Diary_App("zainab", "1234", False)
        my_diary.find_entry(1)
        is_deleted = my_diary.delete_entry(1)
        self.assertFalse(is_deleted)

    def test_exit_from_diary(self):
        Diary_App("zainab", "1234", False)
        self.assertTrue(True)

    def test_view_all(self):
        Diary_App("zainab", "1234", False)
        my_diary.create_entry("Life", "Is a mystery")
        my_diary.view_entry(1)
        expected = """
        =========================
        Id: 1
        Date/Time: 2023-02-04
        
        Title: Ola
        Body: Wale
        ========================="""
        entry = Entry_App("Ola", "Wale", 1)
        self.assertEqual(expected, entry.__str__())

    def test_view_entry(self):
        Diary_App("zainab", "1234", False)
        my_diary.create_entry("Life", "Is a mystery")
        viewed = my_diary.view_entry(1)
        self.assertTrue(viewed)
