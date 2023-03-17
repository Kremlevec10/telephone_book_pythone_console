from view import Menu
from view import MenuItem
from model import TB


def start():
    menu = Menu()
    telephone_book = TB()
    while True:
        menu.show_menu()
        match menu.get_choice():
            case MenuItem.OPEN_TELEPHONE_BOOK.value:
                if not telephone_book.is_opening():
                    telephone_book.open_telephone_book()
                    menu.dislay_message('Вы открыли телефонную книгу')
            case MenuItem.SHOW_CONTACTS.value:
                if telephone_book.is_opening():
                    menu.show_contacts(telephone_book.show_all_contacts())
                else:
                    menu.dislay_message()
            case MenuItem.FINDE_CONTACT.value:
                if telephone_book.is_opening():
                    second_name = menu.find()
                    finde_list = telephone_book.finde_contacts(second_name)
                    menu.show_contacts(finde_list,'Такого контакта нет')
                else:
                    menu.dislay_message()
            case MenuItem.ADD_CONTACT.value:
                if telephone_book.is_opening():
                    contact = menu.add_contact()
                    telephone_book.add_contacts(contact)
                    menu.dislay_message('Контакт добавлен')
                else:
                    menu.dislay_message()
            case MenuItem.UPDATE_CONTACT.value:
                if telephone_book.is_opening():
                    update_contact = menu.update_contatc()
                    update_data = menu.update_data()
                    telephone_book.update_contact(update_contact,update_data)
                    menu.dislay_message('контакт успешно обнавлен')
                else:
                    menu.dislay_message()
            case MenuItem.REMOVE_CONTACT.value:
                if telephone_book.is_opening():
                    data = menu.remove_data()
                    telephone_book.remove_contact(data)
                    menu.dislay_message('Контакт успешно удален')
                else:
                    menu.dislay_message()
            case MenuItem.SAVE_TELEPHONE_BOOK.value:
                if telephone_book.is_opening():
                    telephone_book.save_into_telephone_book()
                    menu.dislay_message('Изменения успешно сохранены')
                else:
                    menu.dislay_message()
            case MenuItem.EXIT.value:
                if telephone_book.is_saving():
                    menu.dislay_message('До скорой встречи')
                    telephone_book.exit()
                else:
                    menu.dislay_message('Сначало сохраните изменения')
