points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    
    path = 0
    if len(coordinates) == 0:
        return (0)
    else:
        for i in range((len(coordinates)-1)):
        
            if coordinates[i] > coordinates[i+1]:
                list = []
                print (coordinates[i])
                print(coordinates[i+1])
                list.append(coordinates[i+1])
                list.append(coordinates[i])
                tlp = tuple(list)
                
                path = path + points.get(tlp)
                print (tlp)
                
            else:
                list = []
                print (coordinates[i])
                print(coordinates[i+1])
                list.append(coordinates[i])
                list.append(coordinates[i+1])
                tlp = tuple(list)
                print (tlp)
                path = path + points.get(tlp)
    return(path)
       
        