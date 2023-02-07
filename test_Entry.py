import unittest
from datetime import date
from unittest import TestCase
from DiaryApp.Entry import Entry_App


class TestEntry(unittest.TestCase):
    TestEntry = Entry_App("Its", "a", "boy")

    def setUp(self) -> None:
        result = self.TestEntry.get_title()
        self.assertEquals("Its", result)

    def test_that_entry_can_have_title(self):
        self.TestEntry.set_title("It's a title")
        result = self.TestEntry.get_title()
        self.assertEquals("It's a title", result)

    def test_that_entry_can_have_body(self):
        self.TestEntry.set_body("The body")
        result = self.TestEntry.get_body()
        self.assertEquals("The body", result)

    def test_that_entry_can_have_date(self):
        result = self.TestEntry.get_date()
        self.assertEqual(date.today(), result)

    def test_that_entry_can_have_identity_number(self):
        self.TestEntry.set_id_number(1)
        result = self.TestEntry.get_id_number()
        self.assertEquals(1, result)


