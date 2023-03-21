import sys
from collections import namedtuple


class TB():
    SECOND_NAME = 'second_name'
    FIRST_NAME = 'first_name'
    PHONE_NUMBER = 'phone_number'
    NOTE = 'note'
    PATH = 'book_test.txt'

    def __init__(self):
        self.__opening = False
        self.__saving = True
        self.__telephone_book: list[namedtuple] = []

    def open_telephone_book(self) -> None:
        with open(TB.PATH, encoding='UTF-8') as file:
            for data in file:
                contact = self.__init_contact(data.strip().split())
                self.__telephone_book.append(contact)
        self.__opening = True

    def save_into_telephone_book(self):
        list_contacts = list(map(lambda x: f'{x.second_name} '
                                           f'{x.first_name} '
                                           f'{x.phone_number} '
                                           f'{x.note}\n'
                                 , self.__telephone_book))
        list_contacts[-1] = list_contacts[-1].strip()
        with open(TB.PATH, 'w', encoding='UTF-8') as file:
            file.writelines(list_contacts)
        self.__saving = True

    def show_all_contacts(self):
        return self.__telephone_book

    def finde_contacts(self, second_name: str) -> list[namedtuple]:
        find_list: list[namedtuple] = list()
        for contact in self.__telephone_book:
            if second_name == contact.second_name:
                find_list.append(contact)
        return find_list

    def add_contacts(self, contact: tuple[str, str, str, str]):
        self.__telephone_book.append(self.__init_contact(contact))
        self.__saving = False

    def update_contact(self, update_contact: tuple[str, str], update_data: namedtuple):
        second_name, first_name = update_contact
        for contact in self.__telephone_book:
            if contact.second_name == second_name and contact.first_name == first_name:
                self.__telephone_book.remove(contact)
                self.__telephone_book.append(update_data)
        self.__saving = False

    def remove_contact(self, remove_data: namedtuple):
        for contact in self.__telephone_book:
            if contact.second_name == remove_data.second_name and contact.first_name == remove_data.first_name:
                self.__telephone_book.remove(contact)
        self.__saving = False

    def exit(self):
        sys.exit()

    def is_opening(self):
        return self.__opening

    def is_saving(self):
        return self.__saving

    def __init_contact(self, data_list: list[str] | tuple[str]) -> namedtuple:
        contact = namedtuple('contact', [TB.SECOND_NAME, TB.FIRST_NAME, TB.PHONE_NUMBER, TB.NOTE])
        return contact(data_list[0], data_list[1], data_list[2], data_list[3])
