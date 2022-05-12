symbols = "0123456789abcdef"
print(symbols[15])
code = [
    '0', '1', '10', '11', '100', '101', '110', '111',
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111',
]
print(code[15])
def formatted_numbers():
    list =["|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary')]
    #print("|{:^10}|{:^10}|{:^10}|".format('decimal', 'hex', 'binary'))
    for i in range(16):
        string = "|{:<10}|{:^10}|{:>10}|".format(i,symbols[i],code[i])
        list.append(string) 
    print(list)
    return(list)
    
for el in formatted_numbers():
    print(el) 
    