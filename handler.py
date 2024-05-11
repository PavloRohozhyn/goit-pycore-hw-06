""" module handler """
from validation import input_error, validation_for_add_function, \
    validation_for_change_function, validation_for_show_function
from utils import print_with_color
from collections import UserDict


@input_error
def parse_input(user_input):
    """ PARSE input data """

    # get command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@validation_for_add_function
def add_contact(args, contacts) -> str | Exception:
    """ ADD contact """

    name, phone = args
    # ADD contact
    contacts[name] = phone
    return "Contact added"


@validation_for_change_function
def change_contact(args, contacts) -> str | Exception:
    """ CHANGE contact """

    name, phone = args
    # CHANGE contact 
    contacts[name] = phone
    return "Contact updated."


@validation_for_show_function
def show_phone(args, contacts) :
    """ show PHONE """

    name, = args
    # show PHONE
    return contacts[name]


def show_all(contacts):
    """ show ALL """

    # contacts = {'foo': '1111', 'bar': '2222', 'tree': '3333'}
    if len(contacts) <= 0:
        print_with_color('Contact book is empty, use "add" command for add contact into book', 'yellow')
    for name, phone in contacts.items():
        print_with_color(f"{name}: {phone}", 'yellow')
    return True



class Field:
    """ class field """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    # реалізація класу
		pass


class Phone(Field):
    # реалізація класу
		pass



class Record:
    """ class record """

    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone:str) -> list[str]:
        """ add phone to list """
        self.phones.append(phone)


    def remove_phone(self, phone):
        """ remove phone from list """
        self.phones.remove(phone)


    def edit_phone(self, phone):
        """ edit phone into list """
        pass 


    def find_phone(self):
        """ find phone into list """ 
        pass



class AddressBook(UserDict):
    """ adress book class """
    data = {}


    def add_record(self, data):
        """ add record into dict """
        self.data.append(data)


    def find(self):
        """ find something into dictionary """
        pass


    def delete(self):
        """ delete somenthing from user dictionary """
        pass
