#luhn's algorithm : 
# 1. check rightmost digit
# 2. double every second digit from the second right most digit
# 3. if doubling makes the number >9, then subtract 9 from the number
# 4. find sum of all digits
# 5. if sum%10==0, then its a valid number otherwise it isnt

num=input("Enter number to be checked : ")
num=list(num)
n=len(num)
num=[int(d) for d in num]
for i in range (n-2, -1, -2):
    num[i]=2*num[i]
    if num[i]>9:
        num[i]=num[i]-9
sum=0
for i in range (0, n):
    sum=sum+num[i]
if sum%10==0:
    print("It's a valid number")
else:
    print("Invalid number")
