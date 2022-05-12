from random import randint
#d = 8
#new_list = []
#list1 =[]
def get_random_password():
    new_list = ''
    for i in range(8):
        random_num = randint(40, 126)
        print(random_num)
        random_num_simbol = chr(random_num)
        print(random_num_simbol)
        new_list = f"{new_list}{random_num_simbol}"
        print (new_list)
    #list_string = str(new_list)
    #return(list_string)
    return(new_list)    
        