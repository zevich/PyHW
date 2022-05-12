articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]

def find_articles(key, letter_case=False):
    print(key)
    print(letter_case)
    new_list = []
    i=0
    for el in articles_dict: 
        if letter_case:
            #new_list = []
            for k,v in el.items():
                
                if type(v) == str:
                    print (v.find(key))
                    if int(v.find(key)) >= 0:
                        new_list.append(el)
                        break
                    else:
                        i =i+1
        else: 
            a = key.lower()
            print(a)
            for k,v in el.items():
                if type(v) == str:
                    b = v.lower()
                    print (b)
                    print(int(b.find(a)))
                    if int(b.find(a)) >= 0:            
                        new_list.append(el)
                        #print(new_list)
                        break        
                    else:
                        i = i+1
                else:
                    break
    print(new_list)
    return(new_list)