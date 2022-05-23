check_list = [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]

def write_employees_to_file(employee_list, path):
    list_1 = [x for l in employee_list for x in l]
    print (list_1)
    file = open(path, 'w')
    for i in list_1:     #for i in employee_list():
        
        file.write(f'{i}\n')
    file.close()

write_employees_to_file(check_list, 'test1.txt')