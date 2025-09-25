#selection sort on a given string
num=input("Enter numbers: ").split()
n=len(num)
for i in range (0, n):
    pos=i
    for j in range (i+1, n):
        if num[j]<num[i]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)

