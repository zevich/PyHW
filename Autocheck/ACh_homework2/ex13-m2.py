message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ord(ch) in range(ord("A"), ord("Z")):
        ch = chr((((ord(ch) - ord("A"))+ offset)%26)+ord("A"))
        encoded_message = encoded_message + ch
    elif ord(ch) in range(ord("a"), ord("z")):
        ch = chr((((ord(ch) - ord("a"))+ offset)%26)+ord("a"))
        encoded_message = encoded_message + ch
        
    else:
        encoded_message = encoded_message + ch