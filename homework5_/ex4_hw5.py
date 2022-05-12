def is_check_name(fullname, first_name):
    print(fullname)
    print(first_name)
    print(fullname.removeprefix(first_name))   # Hook
    if fullname.removeprefix(first_name) == fullname:
        return(False)
    else:
        return(True)