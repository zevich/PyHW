def get_grade(key):
    grades = {
        "F" : 1,
        "FX" : 2,
        "E" : 3,
        "D" : 3,
        "C" : 4,
        "B" : 5,
        "A" : 5
        }
    #key_item = grades[key]
    #print (key_items)
    #return (key_items)
    i = grades.get(key)
    print (i)
    #print (grades.get(key()))
    return(i) 
    
def get_description(key):
    description = {
        "F" : "неудовлетворительно",
        "FX" : "неудовлетворительно",
        "E" : "достаточно",
        "D" : "удовлетворительно",
        "C" : "хорошо",
        "B" : "очень хорошо",
        "A" : "отлично"
        }
        
      #key_items_descr = description.get(key[])
      #print (key_items_descr)
    b =  description.get(key) 
    print (b)
    return (b)
        