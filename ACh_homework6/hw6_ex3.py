def read_employees_from_file(path):
    file = open(path, 'r')
    list = []
    while True:
        line = file.readline()
        if line != '':
            line = line.rstrip()
            list.append(line)
            #print (list)
        if not line:
            break  
    file.close()
    return(list)

read_employees_from_file('test1.txt')
