
n = int(input("Enter the size of the box: "))

for i in range(n):
    for j in range(n):
        # Print stars for the first and last rows, or the first and last columns
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print() 