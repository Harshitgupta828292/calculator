def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b 
operation_dict={
        "+":add ,
        "-":subtract,
        "*":multiply,
        "/":divide
    }
def calculator():
        number1=int(input("enter the first number:"))
        for symbol in operation_dict:
            print(symbol)
        continue_flag=True
        while continue_flag:
            op_symbol=input("pick the operation:")
            number2=int(input("enter the second number:"))
            calculator_function=operation_dict[op_symbol]
            output=calculator_function(number1,number2)
            print(f"{number1}{op_symbol}{number2}={output}")
            should_continue=input(f"enter 'Y' to CONTINUE with {output} or 'N' to start a new calculation and X to exit:").lower()
            if should_continue=='Y':
               number1=output
            elif should_continue=='N':
                    continue_flag=False
                    calculator()
            else:
                continue_flag=False
                print("EXIT SUCCESSFULLY")
calculator()