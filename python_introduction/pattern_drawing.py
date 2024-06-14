size = int(input("Enter the size of the pattern: "))
row = 0
while row < size:
    column = 0
    for column in range(size):
        print("*", end="")
        column += 1
    print()
    row += 1
    



