""" module handler """
from validation import input_error, validation_for_add_function, \
    validation_for_change_function, validation_for_show_function
from utils import print_with_color


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
