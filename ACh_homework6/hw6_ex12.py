import base64


def encode_data_to_base64(data):
    list =[]
    for user in data:
        
        user_bytes = user.encode()
        user_base64_bytes = base64.b64encode(user_bytes)
        
        base64_message = user_base64_bytes.decode("utf-8")

        print(base64_message)
        list.append(base64_message)
    return(list)    
        