size = int(input("Enter the size of the pattern: "))

row = 1
while row <= size:
    for col in range(size):
        print("*", end="")  # print stars side by side
    print()  # move to the next line after each row
    row += 1