# Simple Calculator with Match Case
#print("Enter two numbers one at a time ")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

user_choice = input("Choose the operation, (+, -, *, /): ")

match user_choice:
    case "+":
        print(f"The result is {first_number + second_number}")
    case "-":
        print(f"The result is {first_number - second_number}")
    case "*":
        print(f"The result is {first_number * second_number}")
    case "/":
        if num2 != 0:
            print(f"The result is {first_number / second_number}")
        else:
            print("you cannot divide by zero")
    case _:
        print("you entered an invalid detail")