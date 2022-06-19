from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __repr__(self) -> str:
        return str(self._value)

    def __str__(self) -> str:
        return str(self._value)


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        value = value.strip().removeprefix('+').replace(" ", '').replace("-", '')
        if value.isdigit():
            if len(value) in range(10, 12):
                self._value = value
        else:
            raise ValueError("Not phone")


class Name(Field):
    pass


class Birthday(Field):
    @Field.value.setter
    def value(self, birthday):
        if datetime.strptime(birthday, '%d-%m-%Y'):
            self._value = birthday
        else:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None):
        self.phones = []
        # self.birthdays = []
        self.name = name
        if phone:
            self.add_phone(phone)
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        self.phones.append(phone)

    def change_record_phone(self, phone: Phone, new_phone: Phone):
        if phone.value in [p.value for p in self.phones]:
            self.delete_record_phone(phone)
            self.add_phone(new_phone)

    def delete_record_phone(self, phone: Phone):
        for i, p in enumerate(self.phones):
            if phone.value == p.value:
                self.phones.pop(i)

    def days_to_birthday(self):
        if self.birthday:
            d, m, y = self.birthday.value.split('-')
            start_date_birthday = datetime.now().date()
            end_date_birthday = datetime(day=int(d), month=int(m), year=(start_date_birthday.year)).date()
            delta = (end_date_birthday - start_date_birthday).days
            if delta >= 0:
                return delta
            else:
                return (365 + delta)

    def __repr__(self) -> str:
        return f"{self.name.value} : {', '.join([p.value for p in self.phones])} : {self.birthday.value if self.birthday else ''}"


class AdressBook(UserDict):

    # counter = 0

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def iterator(self):
        counter, print_block = 1, '#' * 25 + '\n'
        for record in self.data.values():
            print_block += str(record) + '\n'
            if counter < 2:  # задаем количество строк вывода
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
    print(f"{name} : {phone} : {birthday}")
    return f'Contact {name} add successful. {delta}  - time to next birthday'


def change(*args):
    name = Name(args[0])
    record = phone_book.get(name.name)
    phone = Phone(args[1])
    new_phone = Phone(args[2])
    record.change_record_phone(phone, new_phone)

    return f"{record.name}'s phone was changed on: {record.phones}"


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
    return f"{record.name} : {record.phones} : {record.birthday}"


COMMANDS = {exit: ["exit", ".", "bye"],
            add: ["add", "добавь", "додай"],
            show_all: ["show all", "show"],
            hello: ["hello"],
            change: ["change"],
            show_contact_phone: ["phone"]
            }


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
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
        # print (phone_book)
        if result[0] is exit:
            break


if __name__ == "__main__":
    main()
    #name = Name("Bill")
    #phone = Phone("0981234567")
    #birthday = Birthday('20-06-1998')

    #rec = Record(name, phone, birthday)

    #print(rec)