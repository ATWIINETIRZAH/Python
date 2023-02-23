import os, random, time

# print("Character Builder")
# name=input("Name your legend: ")

# #def char():
#   chars=input("What's your character?(Human, Elf, Wizard, Orc): ")
#   return char



def rand(number):
  random.randint(1,number)
  return number

def health():
  num=rand(6)
  num1=rand(8)
  hea= ((num*num1)/2) + 10
  return hea

def strength():
  num=rand(6)
  num1=rand(8)
  stre= ((num*num1)/2) + 12
  return stre


while True:
  print("Character Builder")
  name=input("Name your legend: ")
  chars=input("What's your character?(Human, Elf, Wizard, Orc): ")
  strs=strength()
  heaa=health()
  print(name)
  print("HEALTH: ", strs)
  print("STRENGTH: ", heaa)
  
  end=input("do you want to play again?: ")
  if end=="yes" or end=="YES" or end=="Yes":
    continue
  else:
    break
  time.sleep(3)
  os.system("clear")
