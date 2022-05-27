def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
            return result
        except ValueError:
            return "Give me name and phone please1"
        except KeyError:
            return "Enter user name"
        except IndexError:
            return "Give me name and phone please3"

        
    return inner


def my_func_hello(contact: str):
    return "How can I help you?"

def my_func_good_bye(contact: str):
    return "Good bye!"

@input_error
def add_contact(contact: str):
    k,i,c = contact.split(' ')
    contact_dict[i] = c
    print(contact_dict)
    return "Contact saved"

@input_error
def change_contact(contact: str):
    k,i,c = contact.split(' ')
    contact_dict[i] = c
    print (contact_dict)
    return f"Contact changed"

def show_contact_list(contact: str):
    return (contact_dict)

@input_error
def show_phone(contact: str):
    i,c = contact.split(' ')
    return (contact_dict[c])

contact_dict = {}

COMMANDS = {my_func_hello: "hello",
            my_func_good_bye: "good bye. close. exit.",
            add_contact: "add",
            change_contact: "change",
            show_contact_list: "show all",
            show_phone: "phone"
}

def main():
    user_in = " "
    while user_in[-1] != ".":
        user_in = input(">>>").lower()
        for k, v in COMMANDS.items():
            if (v in user_in) or (user_in in v):
                print(k(user_in))
           



if __name__ == "__main__":
    main()