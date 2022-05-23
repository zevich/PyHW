def format_ingredients(items):
    #new_items = items[:]
    if len(items)>1:
        last = items.pop()
        befor_last = items.pop()
        new_element = f"{befor_last} и {last}"
        items.append(new_element)
        result = ", ".join(items)
        print (new_element)
   
    else:
        result = "".join(items)
   
    print (result)
    
    return (result)