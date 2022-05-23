def split_list(grade):
    sum = 0
    list_low = []
    list_up = []
    for i in grade:
        sum = sum + i
    
    if len(grade) == 0:
        return(list_low, list_up)
    else:    
        average = sum // len(grade)
        for i in grade:
            if i <= average:
                list_low.append(i)
            else:
                list_up.append(i)
        print(list_low)
        print(list_up)
        print(list_low, list_up)
        return(list_low, list_up)
   
            
    