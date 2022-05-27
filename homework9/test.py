def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            print("Give me name and phone please1")
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print("Give me name and phone please2")
            result = func(*args, **kwargs)
            return result
        except IndexError:
            print("Give me name and phone please3")
            result = func(*args, **kwargs)
            return result

        
    return inner


def my_func_hello(contact: str):
    return "How can I help you?"

def my_func_good_bye(contact: str):
    return "Good bye!"


def add_contact(contact: str):
    k,i,c = contact.split(' ')
    contact_dict[i] = c
    print(contact_dict)
    return "Contact saved"

def change_contact(contact: str):
    k,i,c = contact.split(' ')
    contact_dict[i] = c
    print (contact_dict)
    return f"Contact changed"

def show_contact_list(contact: str):
    return (contact_dict)

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
@input_error
def main():
    #while
    user_in = " "
    while user_in[-1] != ".":
        user_in = input(">>>").lower()
        for k, v in COMMANDS.items():
            if (v in user_in) or (user_in in v):
                #print (v)
                print(k(user_in))



if __name__ == "__main__":
    main()
    #s=input_error(main)
    #s()




