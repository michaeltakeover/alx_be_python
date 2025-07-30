# Simple Calculator with Match Case
#print("Enter two numbers one at a time ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

user_choice = input("Choose the operation, (+, -, *, /): ")

match user_choice:
    case "+":
        print(f"The result is {num1 + num2}")
    case "-":
        print(f"The result is {num1 - num2}")
    case "*":
        print(f"The result is {num1 * num2}")
    case "/":
        if num2 == 0:
            print(f"The result is {num1 / num2}")
        else:
            print("you cannot divide by zero")
    case _:
        print("you entered an invalid detail")