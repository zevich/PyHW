def is_spam_words(text, spam_words, space_around=False):
    text = text.lower()
    print(text)
    if space_around:
        for word in spam_words:
            word = word.lower()
            print (word)
            if text.find(word) == -1:
                print(False)
                return(False)
            else:
                a = text.find(word)
                print(a)
                print(type(a))
                print (a-1)
                print(text[a-1])
                print(text[a+len(word)])
                if (a == 0 or text[a-1] == " "): # тут нужно дописать проверку на окончание
                #and (text[a+len(word)+1] == " " or text[a+len(word)+1] =="." )):
                  #print(True)
                    return(True)
                else:
                    return(False)
    else:  
        for word in spam_words:
            word = word.lower()
            print (word)
            if text.find(word) == -1:
                print(False)
                return(False)
            else:
                print(True)
                return(True)
    
        