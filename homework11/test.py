from collections import UserDict
from datetime import datetime, timedelta

class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self._value = value
    
    def __repr__(self) -> str:
        return str(self.value)

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
    
    def __repr__(self) -> str:
        return str(self.phone)
    
    @Field.value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError("Not str")
        self._value = value
    
    #def __str__(self) -> str:
        #return f"{self.phone}"

class Name(Field):
    def __init__(self, name):
        self.name = name

class Birthday(Field):
    def __init__(self, birthday):
        self.birthday = birthday

    @Field.value.setter
    def value(self, value):
        if not isinstance(value, int):
            raise ValueError("Not str")
        self._value = value

class Record:
    def __init__(self, name:Name, phone:Phone = None, birthday:Birthday = None):
        self.phones = []
        self.birthdays = []
        self.name = name
        self.phone = phone
        self.birthday = birthday
        if phone:
            self.add_phone(phone)
        elif birthday:
            self.add_birthday(birthday)    

    def add_phone(self, phone:Phone):
        self.phones.append(phone)
    
    def add_birthday(self, birthday:Birthday):
        self.birthdays.append(birthday)

    def change_record_phone(self, phone:Phone, new_phone:Phone):
        if phone.phone in [p.phone for p in self.phones]:
            self.delete_record_phone(phone)
            self.add_phone(new_phone)
        # self.phones.remove(phone)
        # self.phones.append(new_phone)
        # #self.phones.remove(phone)
    
    def delete_record_phone(self, phone:Phone):
        for i, p in enumerate(self.phones):
            if phone.phone == p.phone:
                self.phones.pop(i)
    
    def days_to_birthday(self, birthday:Birthday = None):
        if birthday:
            d, m, y = birthday.split('.')       
            start_date_birthday = datetime.now().date()
            end_date_birthday = datetime(day=int(d), month=int(m), year=(start_date_birthday.year)).date()
            delta = (end_date_birthday - start_date_birthday).days
            if delta >= 0:
                return delta
            else:
                return (365 + delta)

    def __repr__(self) -> str:
        return f"{', '.join([p.phone for p in self.phones])} {', '.join([p.birthday for p in self.birthday])}"


class AdressBook(UserDict):
    
    counter = 0
    
    def add_record(self, record:Record):
        self.data[record.name.name] = record

    def __iter__(self):
        return iter(self.data)

    def __next__(self):
        if self.counter >= len(self.data):
            raise StopIteration()
        result = self.data[self.counter]
        self.counter += 1
        return result

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
    delta = rec.days_to_birthday(birthday.birthday)
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
    
    #for k, v in phone_book.items():
        #result += f'{item}'
    return next(phone_book)
    
    #all_record = []
    #for k, _ in phone_book.items():
        #record = phone_book.get(k)
        #all_record.append(f"{record.name.name} : {record.phones} : {record.birthday.birthday}") 
    return next("\n".join(all_record))

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
    #print(next(phone_book))
        
if __name__ == "__main__":
    main()

#print(next(phone_book))