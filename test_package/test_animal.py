import unittest

from class_animal import Animal


class TestAnimalClass(unittest.TestCase):
    class_Animal = Animal("name", "Yoruba", "100 mile", "run")

    def test_animal_name(self):
        # Given
        self.class_Animal.set_animal_name("Snoopy")
        # When
        result = self.class_Animal.get_animal_name()
        # assert that when I check what get has, check it has snoopy
        self.assertEquals("Snoopy", result)

    def test_animal_speak(self):
        self.class_Animal.set_animal_speak("Yoruba")
        result = self.class_Animal.get_animal_speak()
        self.assertEquals("Yoruba", result)

    def test_animal_dance(self):
        self.class_Animal.set_animal_dance("100 miles")
        result = self.class_Animal.get_animal_dance()
        self.assertEquals("100 miles", result)

    def test_animal_run(self):
        self.class_Animal.set_animal_run(False)
        result = self.class_Animal.get_animal_run()
        self.assertFalse(result)

