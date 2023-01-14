import unittest
from class_in_python.class_list import ClassList


class MyTestCase(unittest.TestCase):

    class_list = ClassList()

    def test_populate_list(self):
        self.class_list.set_length("12", "hi", "me", "[1,2,3]", "get")
        count = self.class_list.get_length()
        self.assertEquals(5, count)

