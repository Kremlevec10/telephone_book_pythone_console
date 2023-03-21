from view import Menu, MenuItem
from model import TB


def start():
    menu = Menu()
    telephone_book = TB()
    while True:
        menu.show_menu()
        match menu.get_choice():
            case MenuItem.OPEN_TELEPHONE_BOOK:
                open_telephone_book(menu, telephone_book)
            case MenuItem.SHOW_CONTACTS:
                show(menu, telephone_book)
            case MenuItem.FINDE_CONTACT:
                fine(menu, telephone_book)
            case MenuItem.ADD_CONTACT:
                add(menu, telephone_book)
            case MenuItem.UPDATE_CONTACT:
                update(menu, telephone_book)
            case MenuItem.REMOVE_CONTACT:
                remove(menu, telephone_book)
            case MenuItem.SAVE_TELEPHONE_BOOK:
                save(menu, telephone_book)
            case MenuItem.EXIT:
                exit(menu, telephone_book)


def open_telephone_book(menu: Menu, telephone_book: TB):
    if not telephone_book.is_opening():
        telephone_book.open_telephone_book()
        menu.dislay_message('***Вы открыли телефонную книгу***')
    else:
        menu.dislay_message('***Вы уже открыли телефонную книгу***')


def show(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        menu.show_contacts(telephone_book.show_all_contacts())
    else:
        menu.dislay_message()


def fine(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        second_name = menu.find()
        if telephone_book.finde_contacts(second_name):
            menu.show_contacts(telephone_book.finde_contacts(second_name))
        else:
            menu.dislay_message('Такой фамилии нет')
    else:
        menu.dislay_message()


def add(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        contact = menu.add_contact()
        telephone_book.add_contacts(contact)
        menu.dislay_message('***Контакт добавлен***')
    else:
        menu.dislay_message()


def update(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        update_contact = menu.update_contatc()
        update_data = menu.update_data()
        telephone_book.update_contact(update_contact, update_data)
        menu.dislay_message('***Контакт успешно обнавлен***')
    else:
        menu.dislay_message()


def remove(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        data = menu.remove_data()
        telephone_book.remove_contact(data)
        menu.dislay_message('***Контакт успешно удален***')
    else:
        menu.dislay_message()


def save(menu: Menu, telephone_book: TB):
    if telephone_book.is_opening():
        telephone_book.save_into_telephone_book()
        menu.dislay_message('***Изменения успешно сохранены***')
    else:
        menu.dislay_message()


def exit(menu: Menu, telephone_book: TB):
    if telephone_book.is_saving():
        menu.dislay_message('***До скорой встречи***')
        telephone_book.exit()
    else:
        menu.dislay_message('***Сначало сохраните изменения***')
