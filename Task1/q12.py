n = int(input("Enter number: "))

# Upper half
for i in range(0, n):  
    for k in range(n-i-1, -1, -1):  
        print(" ", end="")
    for j in range(0, i+1): 
        print("* ", end="")
    print()

# Lower half
for i in range(n-1, -1, -1): 
    for k in range(0, n-i):  
        print(" ", end="")
    for j in range(i+1, 0, -1): 
        print("* ", end="")
    print()
  

#n=4, code will run from 0 to 3

#      *        =3
#     * *       =2
#    * * *      =1
#   * * * *


#n=3, code will run from 0 to 2
#In order to reverse we gotta run it from 2 to 0

