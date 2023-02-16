loan =1000
apr=0.05
counter=0
for i in range(10):
  loan=loan+(apr*loan)
  round(loan,2)
  counter+=1
  print("year",counter,"is",round(loan,2))
print("you paid $",round(loan-1000,2),"in interest")