# *        *    n=8   , *=8
# **      **    n=6   , *=4
# ***    ***    n=4   , *=6
# ****  ****    n=2   , *=8
# **********    n=0   , *=10

n = int(input("Enter number: "))

for i in range(1, n):
    for j in range(0, i):
        print("*", end="")
    for k in range(0, 2 * n - 2 * i - 1):
        print(" ", end="")
    for j in range(0, i):
        print("*", end="")
    print()

for i in range(0, 2 * n - 1):
    print("*", end="")
print()

for i in range(n - 1, 0, -1):
    for j in range(i, 0, -1):
        print("*", end="")
    for j in range(0, 2 * n - 2 * i - 1):
        print(" ", end="")
    for j in range(i, 0, -1):
        print("*", end="")
    print()

