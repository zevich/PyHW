def is_equal_string(utf8_string, utf16_string):
    
    a = utf8_string.decode('utf-8')
    b = utf16_string.decode('utf-16')
    if a ==b:
        return True
    return False