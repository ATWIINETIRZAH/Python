print("Math Game!")
multiple=int(input("Name your multiples: "))
counter=0
for i in range(1,11):
  corr=multiple*i
  print(i,"x",multiple)
  ans=int(input(">>"))
  if ans==corr:
    print("You got it correct!!!")
    counter+=1
  else:
    print("That is wrong. The correct answer should be",corr)
 
if counter==10:
  print("Excellent! You got it all right!")
else:
  print("You got",counter,"out of 10.")
    
