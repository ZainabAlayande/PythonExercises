from unittest import TestCase

from CC.credit_card import doubles_from_behind, sum_two_digit_element_in_a_list, \
    add_the_double_digit_from_back, add_digit_in_the_odd_places, type_of_card, display_card_information, card_number, \
    check_if_card_is_invalid


class Test(TestCase):

    def test_prompt_for_card(self):
        user_card = "4388576018410707"
        the_list = []
        for i in user_card:
            the_list.append(int(i))
        print(the_list)

    def test_doubles_from_behind(self):
        empty_list = [1, 2, 3, 4]
        result = doubles_from_behind()
        self.assertEqual(result, [6, 2])

    def test_sum_two_digit_element_in_a_list(self):
        empty_list = [1, 10, 13, 14, 2, 9, 8, 12]
        result = sum_two_digit_element_in_a_list()
        self.assertEqual(result, [1, 1, 4, 5, 2, 9, 8, 3])

    def test_add_the_double_digit_from_back(self):
        empty_list = [1, 2, 3, 4, 5]
        result = add_the_double_digit_from_back()
        self.assertEqual(result, 15)

    def test_add_digit_in_the_odd_places(self):
        result = add_digit_in_the_odd_places()
        self.assertEquals(result, 8)

    def test_type_of_card(self):
        result = type_of_card()
        self.assertEquals(result, type_of_card())

    def test_display_card_information(self):
        result = display_card_information()
        self.assertEquals(result, display_card_information())

    def test_card_length(self):
        user_card = "4388576018410707"
        length = len(user_card)
        self.assertTrue(length, 16)

    def test_card_number(self):
        result = card_number()
        self.assertTrue(result, card_number())

    def test_check_if_card_is_invalid(self):
        result = check_if_card_is_invalid()
        self.assertFalse(result, result)

