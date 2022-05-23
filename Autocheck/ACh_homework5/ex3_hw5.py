new_phone = (phone.strip()
                .removeprefix('+')
                .replace('(','')
                .replace(')','')
                .replace(' ','')
                .replace('-','') # Первый Уничтожает пробелы, Второй - префиксы
    
    return new_phone