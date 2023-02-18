
import random


print("enter number between 0 and 1,000,000:)")
counter=0
correct_number=random.randint(1,1000)
while True:
  num=int(input("what is your guess?"))
  if num == correct_number:
    print("Correct!")
    counter+=1
    break
  elif num > correct_number:
    print("Too high")
    counter+=1
    continue
  elif num < correct_number and num>0:
    print("too low")
    counter+=1
    continue
  elif num<0:
    exit()
print("it took you",counter,"tries to get it right")
  