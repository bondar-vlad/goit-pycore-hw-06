from collections import UserDict
from processing import PhoneVerificationError

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    def __init__(self, value: str):
        if len(value) == 10:
            super().__init__(value)
        else:
             raise PhoneVerificationError()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
          if not self.find_phone(phone):
               self.phones.append(Phone(phone))

    def remove_phone(self, phone):
          self.phones.remove(self.find_phone(phone))

    def edit_phone(self, old_phone, new_phone):
          self.find_phone(old_phone).value = new_phone

    def find_phone(self, phone):
          phones = list(filter(lambda ph: ph.value == phone, self.phones))
          if len(phones):
               return phones[0]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self, iterable = {}):
          super().__init__(iterable)

    # реалізація класу
          
    def add_record(self, record: Record):
          self.data[record.name.value] = record

    def find(self, name: str) -> Record:
          return self.data.get(name)
    
    def delete(self, name: str):
          self.data.pop(name)