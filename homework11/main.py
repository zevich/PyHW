from collections import UserDict
from datetime import datetime, timedelta

class Field:
    pass
    def __init__(self, value):
        self._value = None
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
    
    
    @Field.value.setter
    def value(self, phone):
        phone = phone.strip().removeprefix('+').replace(" ", '').replace("-", '')
        if phone.isdigit():
            if len(phone) in range(10,12):
                self._value = phone    
        
        else:
            raise ValueError("Not phone")
        
def __repr__(self) -> str:
        return str(self.phone)

class Name(Field):
    def __init__(self, name):
        self.name = name

class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @Field.value.setter
    def value(self, birthday):
        if datetime.datetime.strptime(birthday, '%d-%m-%Y'):
            self._value = birthday
        else:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")
        

class Record:
    def __init__(self, name:Name, phone:Phone = None, birthday:Birthday = None):
        self.phones = []
        #self.birthdays = []
        self.name = name
        self.phone = phone
        self.birthday = birthday
        
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone:Phone):
        self.phones.append(phone)

    def change_record_phone(self, phone:Phone, new_phone:Phone):
        if phone.phone in [p.phone for p in self.phones]:
            self.delete_record_phone(phone)
            self.add_phone(new_phone)
    
    def delete_record_phone(self, phone:Phone):
        for i, p in enumerate(self.phones):
            if phone.phone == p.phone:
                self.phones.pop(i)
    
    def days_to_birthday(self):
        if self.birthday:
            d, m, y = self.birthday.birthday.split('.')       
            start_date_birthday = datetime.now().date()
            end_date_birthday = datetime(day=int(d), month=int(m), year=(start_date_birthday.year)).date()
            delta = (end_date_birthday - start_date_birthday).days
            if delta >= 0:
                return delta
            else:
                return (365 + delta)

    def __repr__(self) -> str:
        return f"{self.name.name} : {', '.join([p.phone for p in self.phones])} : {self.birthday.birthday}"


class AdressBook(UserDict):
    
    #counter = 0
    
    def add_record(self, record:Record):
        self.data[record.name.name] = record

    def iterator(self):
        counter, print_block = 1, '#' * 25 + '\n'
        for record in self.data.values():
            print_block += str(record) + '\n'
            if counter < 2: # задаем количество строк вывода
                counter += 1
            else:
                yield print_block
                counter, print_block = 1, '#' * 25 + '\n'
        yield print_block

phone_book = AdressBook()

def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Sorry, try later.'
    return wrapper

def exit(*args):
    return "Good bye!"

def hello(*args):
    return "How can I help you?"

@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    birthday = Birthday(args[2])
    rec = Record(name, phone, birthday)
    phone_book.add_record(rec)
    delta = rec.days_to_birthday()
    print (f"{name.name} : {phone.phone} : {birthday.birthday}")
    return f'Contact {name.name} add successful. {delta}  - time to next birthday'

def change(*args):
    name = Name(args[0])
    record = phone_book.get(name.name)
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    record.change_record_phone(phone, new_phone)

    return f"{record.name.name}'s phone was changed on: {record.phones}"

def show_all(*args):  
    if not phone_book:
        return 'Address book is empty'
    result = 'USERS LIST:\n'
    print_list = phone_book.iterator()
    for item in print_list:
        result += f'{item}'
    return result

@input_error
def show_contact_phone(*args):
    name = Name(args[0])
    record = phone_book.get(name.name)
    return f"{record.name.name} : {record.phones} : {record.birthday.birthday}"
    
      

COMMANDS = {exit:["exit", ".", "bye"],
            add:["add", "добавь", "додай"],
            show_all:["show all", "show"],
            hello:["hello"],
            change:["change"],
            show_contact_phone:["phone"]
            }

def parse_command(user_input:str):
    for k,v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    
    
def main():
    while True:
        user_input = input(">>>")
        result = parse_command(user_input)
        if not result:
            print("Sorry, unknown command. Try another.")
            continue
        
        print(result[0](*result[1]))
        #print (phone_book)
        if result[0] is exit:
            break

        
if __name__ == "__main__":
    main()

