# MATCH_CASE_CALCULATOR.PY
print("Enter two numbers one at a time ")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

user_choice = input("Choose the operation, (addition, subtraction, multiplication, division): ")

match user_choice:
    case "addition":
        print(f"The result is {num1 + num2}")
    case "subtraction":
        print(f"The result is {num1 - num2}")
    case "multiplication":
        print(f"The result is {num1 * num2}")
    case "division":
        if num2 != 0:
            print(f"The result is {num1 / num2}")
        else:
            print("you cannot divide by zero")
    case _:
        print("you entered an invalid detail")