from collections import UserDict

class Field:
    pass

class Phone(Field):
    def __init__(self, phone):
        self.phone = phone
    
    def __repr__(self) -> str:
        return str(self.phone)
    
    #def __str__(self) -> str:
        #return f"{self.phone}"

class Name(Field):
    def __init__(self, name):
        self.name = name


class Record:
    def __init__(self, name:Name, phone:Phone = None):
        self.phones = []
        self.name = name
        self.phone = phone
        if phone:
            self.add_phone(phone)

    def add_phone(self, phone:Phone):
        self.phones.append(phone)

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
    
    def __repr__(self) -> str:
        return f"{', '.join([p.phone for p in self.phones])}"


class AdressBook(UserDict):
    
    def add_record(self, record:Record):
        self.data[record.name.name] = record

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
    rec = Record(name, phone)
    phone_book.add_record(rec)
    return f'Contact {name.name} add successful'

def change(*args):
    name = Name(args[0])
    record = phone_book.get(name.name)
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    record.change_record_phone(phone, new_phone)

    return f"{record.name.name}'s phone was changed on: {record.phones}"

def show_all(*args):  
    all_record = []
    for k, _ in phone_book.items():
        record = phone_book.get(k)
        all_record.append(f"{record.name.name} : {record.phones}") 
    return "\n".join(all_record)

@input_error
def show_contact_phone(*args):
    name = Name(args[0])
    record = phone_book.get(name.name)
    return f"{record.name.name} : {record.phones}"
    
      

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