def format_string(string="", length=0):
    if length <=len(string):
        print (string)
        return(string)
    else:
        a = (length - len(string)) // 2
        print (a)
        b = " "*a
        print (f"{b}{string}" )
        #return f"{' '*a} {string}"
        return f"{b}{string}"