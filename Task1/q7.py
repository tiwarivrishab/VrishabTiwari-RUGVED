#Write a program to print the Fibonacci Sequence till n-values where n is user input
n=int(input("Enter number of fibonacci values to be printed: "))
sum=1
print("Fibonacci series until "+str(n)+": ")
print("0")
print("1")
pos1=0
pos2=1
for i in range (2, n):
    Sum=pos1+pos2
    print(Sum)
    pos1=pos2
    pos2=Sum


