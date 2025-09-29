#Write a python function to encrypt a string using Caesar’s Cipher (only lowercase)
#A letter is shifted by a fixed number of positions
#Encryption key is the number of spaces by which said shift happens
x=input("Enter string to be encrypted: ")
y=int(input("Enter encryption key: "))
lx=list(x)
n=len(lx)
for i in range (0,n):
    asc=ord(lx[i])
    asc=int(asc)
    asc=asc+y
    if lx[i]==' ':
        continue
    elif asc>122:
        asc=asc-122
        asc=96+asc
        asc=chr(asc)
        lx[i]=asc
    else:asc=chr(asc)
    lx[i]=asc
print("".join(lx))


