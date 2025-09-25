#creating a sorted string
s = input("Enter string to be sorted: ")
sorted_s = " ".join(sorted(s))
print(sorted_s) 
#finding count of each letter
n=len(s)
for i in range (0,n-1):
    count=0
    for j in range (0, n-1):
        if s[i]==s[j]:
            count=count+1
        else: continue
    print(s[i]+" occurs "+str(count)+" times")


