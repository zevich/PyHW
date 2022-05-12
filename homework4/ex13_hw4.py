from pathlib import Path
def parse_folder(path):
    files = []
    folders = []
    
    for i in path.iterdir():
        print (i.name)
        if i.is_file():
           
            files.append(i.name)
            print (files)
        else:
           
            folders.append(i.name)
            print(folders)
       
    return files, folders