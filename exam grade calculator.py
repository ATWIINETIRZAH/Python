print("!!!!Exam Grade Calculator!!!!")
exam=input("enter the name of the exam:")
max=int(input("enter maximum score: "))
score=int(input("enter your score: "))
total=round(score/max*100,2)
if total>=90 and total<=100:
  print("You got",total,"which is an A+")
elif total>=80 and total<=89:
  print("You got",total,"which is an A")
elif total>=70 and total<=79:
  print("You got",total,"which is a B")
elif total>=60 and total<=69:
  print("You got",total,"which is a C")
elif total>=50 and total<=59:
  print("You got",total,"which is a D")
else:
  print("You got",total,"which is a U")