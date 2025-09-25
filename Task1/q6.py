#check whether a given string is an anagram
a=input("Enter string: ")
n=len(a)
flag=0
for i in range (0, n):
    if a[i]!=a[n-i-1]:
        flag=1
if flag==1:
    print("It's not an anagram")
else: print("It's an anagram")
    
    