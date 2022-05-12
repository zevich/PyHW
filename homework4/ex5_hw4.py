def lookup_key(data, value):
    list = []
    for i, val in data.items():
        if val == value:
            list.append(i)
    print (list)
    return (list)