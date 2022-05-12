grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    new_students =[]
    i=1
    for k, v in students.items():
        print(k)
        print (v)
        print(grades[v])
        string = "{:>4}|{:<10}|{:^5}|{:^5}".format(i,k,v,grades[v])
        #string = "{:>4}|{:<10}|{:^5}|{:^5}".format(i,k,v,grades[k])
        print (string)
        new_students.append(string)
        print(new_students)
        i = i+1
    return (new_students)   
    
    
    for el in formatted_grades(students):
        print(el)
    