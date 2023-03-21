from collections import namedtuple
from enum import Enum


class Menu():
    __left_position = 0
    __right_position = 9
    __MENU_TEXT = '''
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
        '''

    def __init__(self):
        self.__choice: int = None

    def show_menu(self) -> None:
        print(Menu.__MENU_TEXT)
        self.__input_menu_item()

    def show_contacts(self, phone_book: list[namedtuple]) -> None:
        for i, contact in enumerate(phone_book):
            print(
                f'{i + 1}. '
                f'{contact.second_name:<20}'
                f'{contact.first_name:<20} '
                f'{contact.phone_number:<20} '
                f'{contact.note:<20}')

    def find(self) -> str:
        second_name = input('Введите фамилию которую хотите найти ')
        return second_name

    def add_contact(self) -> tuple:
        second_name = input('Введите фамилию добавляемого контакта ')
        first_name = input('Введите имя добавляемого контакта ')
        phone_number = input('Введите номер телефона добавляемого контакта ')
        note = input('Введите примечание добавляемого контакта ')
        return second_name, first_name, phone_number, note

    def update_contatc(self) -> tuple:
        second_name = input('Введите фамилию контакта который хотите обновить ')
        first_name = input('Введите имя контакта который хотите обновить ')
        return second_name, first_name

    def update_data(self) -> namedtuple:
        data = namedtuple('contact', 'second_name first_name phone_number note')
        data.second_name = input('Введите новую фамилию ')
        data.first_name = input('Введите новое имя ')
        data.phone_number = input('Введите новый номер ')
        data.note = input('Введите новое примечание ')
        return data

    def remove_data(self) -> namedtuple:
        data = namedtuple('contact', 'second_name first_name')
        data.second_name = input('Введите фамилию контакта который хотите удалить ')
        data.first_name = input('Введите имя контакта который хотите удалить ')
        return data

    def dislay_message(self, message: str = 'Сначало откройте телефонную книгу') -> None:
        print(message)

    def __input_menu_item(self) -> None:
        while True:
            choice = input('Выберите пункт меню ')
            if choice.isdigit() and Menu.__left_position < int(choice) < Menu.__right_position:
                self.__choice = self.__get_menu_item(int(choice))
                print('\n')
                break
            else:
                print('Вы ввели неверный формат ')

    def __get_menu_item(self, choice: int):
        match choice:
            case MenuItem.OPEN_TELEPHONE_BOOK.value:
                return MenuItem.OPEN_TELEPHONE_BOOK
            case MenuItem.SHOW_CONTACTS.value:
                return MenuItem.SHOW_CONTACTS
            case MenuItem.FINDE_CONTACT.value:
                return MenuItem.FINDE_CONTACT
            case MenuItem.ADD_CONTACT.value:
                return MenuItem.ADD_CONTACT
            case MenuItem.UPDATE_CONTACT.value:
                return MenuItem.UPDATE_CONTACT
            case MenuItem.REMOVE_CONTACT.value:
                return MenuItem.REMOVE_CONTACT
            case MenuItem.SAVE_TELEPHONE_BOOK.value:
                return MenuItem.SAVE_TELEPHONE_BOOK
            case MenuItem.EXIT.value:
                return MenuItem.EXIT

    def get_choice(self) -> MenuItem:
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
