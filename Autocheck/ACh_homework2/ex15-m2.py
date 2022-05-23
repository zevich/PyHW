result = None
operand = None
operator = None
wait_for_number = True

result = int(input("Введите число :"))
while True:
    if wait_for_number:
        operator = input("Введите операцию '+', '-', '*','/': ")

        if operator == "=":
            result    
            break
        
        if not (operator == "+" or operator == "-" or operator == "*" or operator == "/"):
            print(f" {operator} is not '+' or '-' or '/' or '*'. Try again")
            continue
        
        else:
            wait_for_number = not wait_for_number

    else:
        
        operand = input("Введите число:")
        try:
            operand = int(operand)
        except ValueError:
            print(f" {operand} is not a number. Try again.")
            continue
        
        if operator == "+":
            result = result + operand
        
        if operator == "-":
            result = result - operand
            
        if operator == "/":
            result = result/operand
            
        if operator == "*":
            result = result*operand

        wait_for_number = not wait_for_number    