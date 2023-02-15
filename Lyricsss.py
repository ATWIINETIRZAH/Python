print("Fill in the blank lyrics! (Type in the blank lyrics and see if you are a s cool as me>>>")
counter=1
while True:
  print("Never going to____ you up.")
  ans=input("enter answer: ")
  if ans!="give":
    print("Nope,try again!")
    counter +=1
  else:
    print("Well done! ")
    break
print("it only took you",counter,"tries.")