def prepare_data(data): 
    new_data = sorted(data)
    deleted_sign = new_data.pop(0)
    deleted_sign = new_data.pop()
    
    return(new_data)