from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Invalid command format."
        except IndexError:
            return "Contact not found."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

@input_error
def contact_phone(args, contacts: dict):
    name = args[0]
    return contacts.get(name, "Contact not found.")

@input_error
def all_contacts(contacts: dict):
    return "\n".join(list(contacts.values()))


