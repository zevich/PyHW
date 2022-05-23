def save_applicant_data(source, output):
    with open(output, 'w') as fileoutput:
        a = 0
        print(len(source))
        for abitur in source:
            #print (abitur)
            a += 1
            list = []
            for k,v in abitur.items():
                #print (v)
                list.append(str(v))
            print (list)
            string = ",".join(list)
            print(string)
            if a != len(source):    
                fileoutput.writelines(string + '\n')
            else:
                fileoutput.writelines(string)
            string =''
    return(fileoutput)
            
                
            