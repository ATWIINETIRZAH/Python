import random
sides=int(input("how many sides should the dice be?: "))
ans="yes"

def rollDice(sides):
  print("you rolled",random.randint(1,sides))
while ans=="yes" :
  rollDice(sides)
  ans=input("Do you want to roll the dice again?: ")
  
      
rollDice()