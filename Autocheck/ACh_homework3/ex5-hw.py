#middle_name=None
def get_fullname (first_name, last_name, middle_name = None):
    if middle_name:
       # print (f" {first_name } {middle_name } {last_name}")
        return(f"{first_name} {middle_name} {last_name}")
    else: 
       # print (f"{first_name } {last_name}")
        return(f"{first_name} {last_name}")

    
        