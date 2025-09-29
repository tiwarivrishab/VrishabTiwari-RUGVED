#Using Coleman-Luhn's formula to find grade point level
# 1. Count total number of letters, no special characters or spaces
# 2. Count total number of words
# 3. Count total number of sentences
# 4. L = Letters/Words * 100
# 5. S = Sentences/Wprds * 100
# 6. Ans = 0.0588 × L − 0.296 × S − 15.8

import string
import re
og=input("Enter the text: ")

#words:
words=float(len(og.split()))
print("No of words: " + str(words))

#letters:
table=str.maketrans("","", string.punctuation + " ")
og1=og.translate(table)
letters=float(len(og1))
print("No of letters are: " + str(letters))

#sentences:
og2=re.split('[.?!]', og)
og2 = [x for x in og2 if x != '']
print(og2)
sentences=float(len(og2))
print("Sentences: " + str(sentences))

#calculations:
l=float((letters/words)*100)
s=float((sentences/words)*100)
print("l=" +str(l))
print("s="+str(s))
print("Ans = float(0.0588 * l - 0.296 * s - 15.8)")
Ans = float(0.0588 * l - 0.296 * s - 15.8)
print("Answer is :"+str(Ans))

