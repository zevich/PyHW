import re

def sanitize_file(source, output):
    with open(source, 'r') as filesource:
        text = filesource.read()
        sanitize_string = re.sub(r'\d+', '', text)
        #print (sanitize_string)
    with open(output, 'w') as fileoutput:
        fileoutput.write(sanitize_string)
        
            
    
    
        
            
    
        
