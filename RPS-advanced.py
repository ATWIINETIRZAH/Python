from getpass import getpass as input

counter1=0
counter2=0
print("!!EPIC BATTLE!!")
print("R for Rock,P for paper,S for Scissors")

while True:
  
  player1=input("Enter your move: ")
  player2=input("Enter your move: ")
  
  if player1=="R":
    if player2=="S":
      print("player 1's rock beats player2's scissors")
      counter1+=1
    elif player2=="P":
      print("player2's paper beats player1's rock")
      counter2+=0
    elif player2=="R":
      print("its a draw! Play again.")
    else:
      print("Enter either R,P,or S")
  elif player1=="P":
    if player2=="S":
      print("Player2's scissors beat player1's paper")
      counter2+=0
    elif player2=="R":
      print("Player1's paper beats player2's Rock ")
      counter1+=1
    elif player2=="P":
      print("its a draw! Play again.")
    else:
      print("Enter either R,P,or S")
  elif player1=="S":
    if player2=="P":
      print("player1's scissors beat player2's paper")
      counter1+=1
    elif player2=="R":
      print("player2's rock beats player1's scissors")
      counter2+=0
    elif player2=="S":
      print("its a draw! Play again.")
    else:
      print("Enter either R,P,or S")
  else:
    print("Enter either R,P,or S")
  if counter1==3:
    print("Player1 wins this game with",counter1,"points:)")
    break
  elif counter2==3:
    print("player2 wins the game with",counter2,"points:)")
    break
  else:
    continue