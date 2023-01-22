class CreditCard:
    def __init__(self):
        pass


empty_list = []
double_digit_list = []
new_lst = []
user_number = 0


def prompt_for_card():
    user_card_number = input("Hello, Kindly enter card details to verify: ")

    for each_letter in user_card_number:
        empty_list.append(int(each_letter))

    return empty_list


def doubles_from_behind():
    for j in range(0, len(empty_list), 2):
        double_digit_list.append(int(empty_list[j]) * 2)

    return double_digit_list[::-1]


def sum_two_digit_element_in_a_list():
    for i in double_digit_list:
        if i > 9:
            digits = [int(d) for d in str(i)]
            new_lst.append(sum(digits))
        else:
            new_lst.append(i)

        return new_lst[::-1]


def add_the_double_digit_from_back():  # 37
    sum_it = 0
    for i in new_lst:
        sum_it = sum_it + i

    return sum_it


def add_digit_in_the_odd_places():  # 38
    add_up = 0
    for i in range(-1, -len(empty_list) - 1, -2):
        add_up += empty_list[i]

    return add_up


def type_of_card():
    if empty_list[0] == 4:
        print("Visa Card")

    elif empty_list[0] == 5:
        print("Master Card")

    elif empty_list[0] == 3 and empty_list[1] == 7:
        print("American Visa Card")

    elif empty_list[0] == 6:
        print("Discover Card")

    else:
        print("Invalid Card")


def display_card_information():
    print()
    print("******************************************")
    print("**Credit Card Type: ", end="")
    type_of_card()
    print("**Credit Card Number: ", card_number())
    print("**Credit Card Length: ", card_length())
    print("**Credit Card Validity Status: ", end='')
    check_if_card_is_invalid()
    print("******************************************")


def card_length():
    return len(empty_list)


def card_number():
    return int("".join(str(i) for i in empty_list))


def check_if_card_is_invalid():
    response_one = (add_the_double_digit_from_back() + add_digit_in_the_odd_places()) % 10 == 0
    response_two = (add_the_double_digit_from_back() + add_digit_in_the_odd_places()) % 10 != 0

    if response_one:
        print("Valid")

    if response_two:
        print("Invalid")


prompt_for_card()
display_card_information()
