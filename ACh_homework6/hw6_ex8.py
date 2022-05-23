abitur_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    with open(output, 'w') as fileoutput:
        a = 0
        for abitur in source:
            print (abitur)
            #string = ''
            a +=1
            list = []
            for k,v in abitur.items():
                print (v)
                list.append(str(v))
            print (list)
            string = ",".join(list)
            print(string)
            if a != len(source):    
                fileoutput.writelines(string + '\n')
            else:
                fileoutput.writelines(string)
            string =''
    #return(fileoutput)

save_applicant_data(abitur_list, "output.txt")       
                
            