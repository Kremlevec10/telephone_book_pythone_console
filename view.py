from collections import namedtuple
from enum import Enum


class Menu():
    __LEFT_POSITION = 0
    __RIGHTH_POSITION = 9

    def __init__(self):
        self.__choice: int = None

    def show_menu(self):
        print('''
Рады видеть вас в нашей телефонной книге "СтоунГрупп"
    Выберите пункт меню:
        1. Открыть телефонную книгу
        2. Показать контакты
        3. Найти контакт
        4. Добавить контакт
        5. Обновить контакт
        6. Удалить контакт
        7. Сохранить изменения
        8. Выход
        ''')
        self.__input_menu_item()

    def show_contacts(self, phone_book: list[dict]):
        if phone_book:
            for i, contact in enumerate(phone_book):
                print(
                    f'{i + 1}. '
                    f'{contact["second_name"]:<20}'
                    f'{contact["first_name"]:<20} '
                    f'{contact["phone_number"]:<20} '
                    f'{contact["note"]:<20}')

    def find(self):
        second_name = input('Введите фамилию которую хотите найти ')
        return second_name

    def add_contact(self):
        second_name = input('Введите фамилию добавляемого контакта ')
        first_name = input('Введите имя добавляемого контакта ')
        phone_number = input('Введите номер телефона добавляемого контакта ')
        note = input('Введите примечание добавляемого контакта ')
        return second_name, first_name, phone_number, note

    def update_contatc(self):
        second_name = input('Введите фамилию контакта который хотите обновить ')
        first_name = input('Введите имя контакта который хотите обновить ')
        return second_name, first_name

    def update_data(self) -> namedtuple:
        second_name = input('Введите новую фамилию ')
        first_name = input('Введите новое имя ')
        phone_number = input('Введите новый номер ')
        note = input('Введите новое примечание ')
        data = namedtuple('contact', 'second_name first_name phone_number note')
        data.second_name = second_name
        data.first_name = first_name
        data.phone_number = phone_number
        data.note = note
        return data

    def remove_data(self) -> namedtuple:
        data = namedtuple('contact', 'second_name first_name')
        data.second_name = input('Введите фамилию контакта который хотите удалить ')
        data.first_name = input('Введите имя контакта который хотите удалить ')
        return data

    def dislay_message(self, message: str = 'Сначало откройте телефонную книгу'):
        print(message)

    def __input_menu_item(self):
        while True:
            choice = input('Выберите пункт меню ')
            if choice.isdigit() and Menu.__LEFT_POSITION < int(choice) < Menu.__RIGHTH_POSITION:
                self.__choice = int(choice)
                break
            else:
                print('Вы ввели неверный формат ')

    def get_choice(self) -> int:
        return self.__choice


class MenuItem(Enum):
    OPEN_TELEPHONE_BOOK = 1
    SHOW_CONTACTS = 2
    FINDE_CONTACT = 3
    ADD_CONTACT = 4
    UPDATE_CONTACT = 5
    REMOVE_CONTACT = 6
    SAVE_TELEPHONE_BOOK = 7
    EXIT = 8
