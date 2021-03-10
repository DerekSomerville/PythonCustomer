import random

def numgen(): #gets a random digit
   number = random.randint(0,9)
   return str(number)

def ordercode():#makes a random 6 digit number
   ordernum = numgen() + numgen() + numgen() + numgen() + numgen() + numgen()
   return ordernum


with open("ordernum.txt") as file:
    ordernumber = [line.rstrip() for line in file]
    file.close
newcode = ordercode()
inuse = True

while inuse == True:
   if newcode in ordernumber:
      newcode = ordercode()
   else:
      inuse = False
      file = open("ordernum.txt", "a")
      file.write("\n"+ newcode)
      file.close


