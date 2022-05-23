def real_len(text):
    #if text.find()
    print(len(text))
    b = 0
    for i in (range(len(text))):
        if text[i] == '\n' or text[i] == '\f' \
        or text[i] == '\r' or text[i] == '\t' \
        or text[i] == '\v': 
        # and text[i+1] =='n':
            b = b + 1
            print (b)
    result = len(text) - b
    print(result)
    
    return result
        
      
    
    
        
            
    
    