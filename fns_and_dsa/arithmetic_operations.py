
def perform_operation(num1, num2, operation:str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 -  num2
    elif operation == "multiply":
        return num1 * num2 * operation
    elif operation == "divide":
        if num2 == 0:
            return "Error: ZeroDivisionError"
        return num1 / num2
    else:
        return "Error: Invalid Input"