import sys
from collections import namedtuple


class TB():
    SECOND_NAME = 'second_name'
    FIRST_NAME = 'first_name'
    PHONE_NUMBER = 'phone_number'
    NOTE = 'note'

    def __init__(self):
        self.__opening = False
        self.__saving = True
        self.__telephone_book: list[dict] = list()
        self.__path = 'book_test.txt'

    def open_telephone_book(self):
        with open(self.__path, encoding='UTF-8') as file:
            for data in file:
                data_list = data.strip().split()
                contact = {TB.SECOND_NAME: data_list[0], TB.FIRST_NAME: data_list[1],
                           TB.PHONE_NUMBER: data_list[2], TB.NOTE: data_list[3]}
                self.__telephone_book.append(contact)
        self.__opening = True

    def save_into_telephone_book(self):
        list_contacts = list(map(lambda x: f'{x.get(TB.SECOND_NAME)} '
                                           f'{x.get(TB.FIRST_NAME)} '
                                           f'{x.get(TB.PHONE_NUMBER)} '
                                           f'{x.get(TB.NOTE)}\n'
                                 , self.__telephone_book))

        with open(self.__path, 'w', encoding='UTF-8') as file:
            file.writelines(list_contacts)
        self.__saving = True

    def show_all_contacts(self):
        return self.__telephone_book

    def finde_contacts(self, second_name: str):
        find_list = list()
        for contact in self.__telephone_book:
            if second_name == contact[TB.SECOND_NAME]:
                find_list.append(contact)
        return find_list if find_list is not None else 'Такой фамилии нет'

    def add_contacts(self, contact: tuple) -> str:
        second_name, first_name, phone_number, note = contact
        self.__telephone_book.append(
            {TB.SECOND_NAME: second_name, TB.FIRST_NAME: first_name,
             TB.PHONE_NUMBER: phone_number, TB.NOTE: note})
        self.__saving = False

    def update_contact(self, update_contact: tuple, update_data: namedtuple):
        second_name, first_name = update_contact
        for contact in self.__telephone_book:
            if contact.get(TB.SECOND_NAME) == second_name and contact.get(TB.FIRST_NAME) == first_name:
                contact[TB.SECOND_NAME] = update_data.second_name
                contact[TB.FIRST_NAME] = update_data.first_name
                contact[TB.PHONE_NUMBER] = update_data.phone_number
                contact[TB.NOTE] = update_data.note
        self.__saving = False

    def remove_contact(self, remove_data: namedtuple):
        for contact in self.__telephone_book:
            if contact.get(TB.SECOND_NAME) == remove_data.second_name and contact.get(
                    TB.FIRST_NAME) == remove_data.first_name:
                self.__telephone_book.remove(contact)
        self.__saving = False
        return 'Контакт удален'

    def exit(self):
        sys.exit()

    def is_opening(self):
        return self.__opening

    def is_saving(self):
        return self.__saving
