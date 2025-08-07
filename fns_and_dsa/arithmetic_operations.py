'''python .\main.py
Arithmetic Operations
Enter the first number: 5
Enter the second number: 6
Enter the operation (add, subtract, multiply, divide): add
Result: 11.0
# arithmetic_operations.py
def Performe_Operation():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    #print(f"add = {num1 + num2}")
    '''
def perform_operation(num1:float, num2:float, operation:str):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 -  num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "" "Error: ZeroDivisionError"
    else:
        return "Invalid Input"