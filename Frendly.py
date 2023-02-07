import pickle
from DiaryApp.Diary import Diary_App

my_diary = Diary_App("zainab", "1234", False)


def load_diary():
    pass


def create_moment(self=None):
    create_title = input("Enter title for moment: ")
    create_body = input("Enter the body: ")
    my_diary.create_entry(create_title, create_body)
    print()
    print("Moment created successfully")
    print("Keep creating moment")
    main_menu()


def view_moment(self=None):
    try:
        moment_to_be_viewed = int(input("Enter moment to be viewed: "))
        print(my_diary.view_entry(moment_to_be_viewed))
        print()
    except IndexError:
        print("Id doesn't exist")

    finally:
        main_menu()


def edit_moment():
    try:
        moment_to_be_edited = int(input("Enter memory id to be edited: "))
        my_diary.validate_id(moment_to_be_edited)
        title = input("Enter a new title: ")
        body = input("Enter a  new body: ")
        my_diary.edit_entry(moment_to_be_edited, title, body)
        print("You edited moment", moment_to_be_edited)
        print("")
    except IndexError:
        print("Id doesn't exist")

    finally:
        main_menu()


def count_moment(self=None):
    print("""
    You have created """, my_diary.get_count_of_entry_created(), """ so far
    Keep more moments coming
    Frendly gat you all day long """)
    main_menu()


def exit_diary(self=None):
    pass
    # save_diary()
    # my_diary.close_diary()


def view_all_moments(self=None):
    my_diary.view_all_entry()
    main_menu()


def delete_moment(self=None):
    try:
        moment_to_be_deleted = int(input("Enter you wish to delete: "))
        my_diary.validate_id(moment_to_be_deleted)
        print("You are about to delete moment", moment_to_be_deleted)
        print(my_diary.view_entry(moment_to_be_deleted))
        temp = int(input("""
        Press 1 --> to proceed
        Press 2 --> to stop delete """))
        if temp == 1:
            my_diary.delete_entry(moment_to_be_deleted)
            print("Moment ", moment_to_be_deleted, " successfully deleted")
        elif temp == 2:
            main_menu()
    except IndexError:
        print("Id doesn't exist")
        main_menu()

    finally:
        main_menu()


def save_diary():
    with open("diary.pkl", 'wb') as file:
        pickle.dump(my_diary, file)
        file.close()
        print("File saved")



def main_menu():
    # load_diary()
    first_display()
    user_input = int(input("""
    Welcome to Friendly Diary App
    1 -> Create moment
    2 -> View moment
    3 -> Update moment
    4 -> Count moments
    5 -> View All moment
    6 -> Delete Moments
    7 -> Exit    
        """))

    if user_input == 1:
        create_moment()

    elif user_input == 2:
        view_moment()

    elif user_input == 3:
        edit_moment()

    elif user_input == 4:
        count_moment()

    elif user_input == 5:
        view_all_moments()

    elif user_input == 6:
        delete_moment()

    elif user_input == 7:
        save_diary()
        exit_diary()

    else:
        print("Invalid number")
        main_menu()


def first_display():
    print("""
    ________________________________
        YOUR FRENDLY DIARY APP
    ________________________________
    --------------------------------
    """)


if __name__ == '__main__':
    try:
        with open("diary.pkl", 'rb') as new_file:
            my_diary = pickle.load(new_file)
            print("i AM TAYAD")
            print(my_diary.get_count_of_entry_created())

    except FileNotFoundError:
        print()
    main_menu()
