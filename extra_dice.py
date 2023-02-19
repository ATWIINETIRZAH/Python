import random
roll="yes"

def Dice(number):
  number=random.randint(1,number)
  return number
  
d=Dice(20)
print(d)

def SubR():
  num1=Dice(6)
  num2=Dice(8)
  hea= num1*num2
  return hea


while roll=="yes":
  name=input("Name your warrior: ")
  hea=str(SubR())
  print("Their health is ",hea,"hp")
  roll=input("Do you want to try again?")
  
  