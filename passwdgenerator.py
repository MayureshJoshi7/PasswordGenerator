@author: Mayuresh
"""

import random
import re
chars='abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
password=""
n=int(input("How many letters do you need in your password ?"))
for i in range(1,n+1):
    password+=random.choice(chars)
    reg=re.compile('!@#$%^&*()1234567890')
print(password)
if(reg.search(password)==0):
        print("Not enough special characters and numbers, Weak password\nPlease Regenerate...")
else:
    if(n<=7):
        print("Password can be stronger")
    elif(n<=3 ):
        print("Weak Password!!")
    elif(n>=9):
        print("Congrats! password is strong!")