def get_credentials_users(path):
    list = []
    with open(path, 'rb') as file:
        while True:
            line = file.readline().rstrip().decode()
            #line = line.decode()
            if line != '':
                print(line)
                list.append(line)
            if not line:
                break
    print(list)
    return (list)