def get_recipe(path, search_id):    
    dict = {
    }
    #list = []
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if line != '':
                line = line.rstrip()
                line = line.split(',')
                print(line)
                if line[0] == search_id:
                    dict['id'] = line[0]
                    dict['name'] = line[1]
                    dict['ingredients'] = line[2::1]
                print(dict)
            
            if not line:
                break    
    if dict == {}:
       dict = None
    return (dict)           
            
            