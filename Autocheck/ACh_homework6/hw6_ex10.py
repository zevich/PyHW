dict = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}
def save_credentials_users(path, users_info):
    print (users_info)
    with open(path, 'wb') as file:
           
        for username, password in users_info.items():
            print(f' {username}:{password}')
            a = f'{username}:{password}\n'.encode()
            file.write(a)

save_credentials_users('hwex10.bin', dict)