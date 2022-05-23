def total_salary(path):
    sum = 0
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        if line != '':
            print(line)
            d, m = line.split(',')
            print(d)
            print (m)
            sum += float(m)
            print (sum)
        if not line:
            break  
    print (sum)
    fh.close()
    
total_salary('test.txt')
      
            
            
    
        
    
