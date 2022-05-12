def is_valid_pin_codes(pin_codes):
    my_set = set(pin_codes)
    print (my_set) 
    
    if len(pin_codes) == 0:
        return (False)
    
    else:
        if len(pin_codes) == len (my_set):
            sum = 0
            for i in my_set:
                #print(i)
                if type(i) == str and len(i) == 4 and i.isdigit():
                    sum = sum + 1
            if len(my_set) == sum:
                return (True)
            else:
                return (False)
        else:
            return (False)
        
        
    