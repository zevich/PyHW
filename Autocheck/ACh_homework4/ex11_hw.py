from random import randint


def get_random_password():
    result = ""
    count = 0
    while count < 8:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if ch >= "A" and ch <= "Z":
            has_upper = True
        elif ch >= "a" and ch <= "z":
            has_lower = True
        elif ch >= "0" and ch <= "9":
            has_num = True
    if len(password) == 8 and has_upper and has_lower and has_num:
        return True
    else:
        return False


def get_password():
    
   
    count = 0
    while count < 100:
        password1 = get_random_password()
        print (password1)
        print(is_valid_password(password1))
        
        if is_valid_password(password1):
            print(password1)
            return(password1)
             
            break
        
        else:
            count = count + 1
            print (count)
           