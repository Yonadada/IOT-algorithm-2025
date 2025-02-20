# calculator.py
# BLUEPRINT | DONT EDIT
playing = True


# /BLUEPRINT

# 👇🏻 YOUR CODE 👇🏻:
    

while playing:
    a = int(input("Choose a number: "))
    b = int(input("Choose another one: "))
    operation = input(
    "Choose an operation:\n    Options are: + , - , * or /.\n    Write 'exit' to finish.\n")
    
    if operation == '+':
        result = a+b 
        result = print(f'Result = {a+b}')
        

    elif operation == '-':
        result = a-b
        result = print(f'Result = {a-b}')
    
    
    elif operation == '/':
        result = a/b
        result = print(f'Reuslt = {a/b}')
        
    
    elif operation == '*':
        result = a*b
        result = print(f'Result = {a*b}')
        
    
    elif operation == "exit".lower():
        break
    
    else:
        break
        

# /YOUR CODE



