import shutil


def create_backup(path, file_name, employee_residence):
    with open(path+'/'+ file_name, 'wb') as file:
        for username, country in employee_residence.items():
            print(f'{username} {country}')
            a = f'{username} {country}\n'.encode()
            #print(a)
            file.write(a)
            
        archive_name = shutil.make_archive('backup_folder', 'zip',path)
    print (archive_name)
    return(archive_name)
        
            
    