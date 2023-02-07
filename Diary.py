import sys
from DiaryApp.Entry import Entry_App

list_of_entries = []


class Diary_App:

    def __init__(self, username: str, password: str, is_locked: bool):
        self.username = username
        self.password = password
        self.is_locked = is_locked

    def set_username(self, username: str):
        self.username = username

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def unlock_diary(self):
        return self.password

    def lock_diary(self, is_locked):
        self.is_locked = is_locked

    def is_locked(self):
        return self.is_locked

    def create_entry(self, title, body):
        identity_number = len(list_of_entries) + 1
        my_entry = Entry_App(title, body, identity_number)
        list_of_entries.append(my_entry)

    def view_entry(self, identity_number: int):
        self.validate_id(identity_number)
        return list_of_entries.__getitem__(identity_number - 1)

    def edit_entry(self, identity_number: int, title: str, body: str):
        self.validate_id(identity_number)
        diary = Diary_App("zainab", 1234)
        my_entry = Entry_App(body, title, identity_number)
        for i in list_of_entries:
            if list_of_entries.__getitem__(i).__getitem__(identity_number) == identity_number:
                list_of_entries.__getitem__(i).set_title(title)
                list_of_entries.__getitem__(i).set_body(body)

    def validate_id(self, identity_number):
        if identity_number <= 0 or identity_number > len(list_of_entries):
            raise IndexError

    def get_count_of_entry_created(self):
        return len(list_of_entries)

    def delete_entry(self, identity_number):
        self.validate_id(identity_number)
        if identity_number in list_of_entries:
            list_of_entries.remove(identity_number)

    def view_all_entry(self):
        for i in list_of_entries:
            print(i)

    def find_entry(self, identity_number: int):
        return list_of_entries.__contains__(identity_number)

    def close_diary(self):
        return sys.exit()
