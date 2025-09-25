#ex: Hill Number : 1234321 --> 1234 going up then 4321 coming down
num=input("Enter number to check: ")
n=len(num)
flag=0
for i in range (0, n):
    if num[i]!=num[n-i-1]:
        flag=1
        break
if flag==1:
    print("Not a hill number")
else: print("Its a hill number")
