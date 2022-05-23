def get_cats_info(path):
    #file = open(path, 'r')
    dict = {
        'id' : None,
        'name' : None,
        'age' : None}
    list = []
    with open(path, 'r') as file:
    
        while True:
            line = file.readline()
            if line != '':
                #print(line)
                line = line.rstrip()
                id1, name, age = line.split(',')
                print (f'{id1} - {name} - {age}')
                dict['id'] = id1
                dict['name'] = name
                dict['age'] = age
                list.append(dict)
                dict = {}
                print(list)
          
            if not line:
                break
        
    return (list)       
            
    
