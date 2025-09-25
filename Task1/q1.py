a=input("Enter true or false: ")
b=input("Enter true or false: ")
c=input("Enter true or false: ")
def triple_and(a,b,c):
    if a.lower()==b.lower()==c.lower()=="true":
        return True
    else: return False
print(triple_and(a,b,c))
