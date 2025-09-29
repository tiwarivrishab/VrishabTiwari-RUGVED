n=int(input("Enter number: "))
for i in range (0, n, +1):
    for k in range (n-i-1, -1, -1):
        print(" ", end="")
    for j in range (0, i+1, +1):
        print("*", end=" ")
    print("\n")