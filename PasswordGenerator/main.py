
import string
import random

# Using the diffrent types of string variations possible 

string1=list(string.ascii_lowercase)
string2=list(string.ascii_uppercase)
    
# taking care of the punctuations combinations
   
string3=list(string.punctuation)

    
userInput=int(input("Please enter the length of the password:\n"))


if(userInput>0):
      s=[]
      s.extend((string1))
      s.extend((string2))
      s.extend((string3))
      random.shuffle(s)

      password=("".join(s[0:userInput]))

      print(f"Your randomnly generated password is {password}")
 
else:
    print("Enter a value greater than 0 ")  

