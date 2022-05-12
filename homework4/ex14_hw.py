import sys


def parse_args():
    result = ""
    for arg in sys.argv:
        print(arg)
        
        result = f"{result} {arg}"
        print (result)
    words = result.split(' ')    
    
    print(words)
    words = words[2:]
    words1 = " ".join(words)
    
    return (words1)