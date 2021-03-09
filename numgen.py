import random

def numgen(): #gets a random digit
   number = random.randint(0,9)
   return str(number)

#makes a rondom 6 digit orger number
ordernum = numgen() + numgen() + numgen()+ numgen()+ numgen()+ numgen()
print(ordernum)
