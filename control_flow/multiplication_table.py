# MULTIPLICATION_TABLE.PY

number = input("Enter a number to see its multiplication: ")

for i in range(1, 13):
    for number in range(1, 10):
        product = i * number
    #print(f"{i} * {number} = {product}", end="\t")
    print(i, "*", number, "=", product, end="\t")
    print()
