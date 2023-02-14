from getpass import getpass as input

print("!!EPIC BATTLE!!")
print("R for Rock,P for paper,S for Scissors")

player1=input("Enter your move: ")
player2=input("Enter your move: ")

if player1=="R":
  if player2=="S":
    print("player 1's rock beats player2's scissors")
  elif player2=="P":
    print("player2's paper beats player1's rock")
  elif player2=="R":
    print("its a draw! Play again.")
  else:
    print("Enter either R,P,or S")
elif player1=="P":
  if player2=="S":
    print("Player2's scissors beat player1's paper")
  elif player2=="R":
    print("Player1's paper beats player2's Rock ")
  elif player2=="P":
    print("its a draw! Play again.")
  else:
    print("Enter either R,P,or S")
elif player1=="S":
  if player2=="P":
    print("player1's scissors beat player2's paper")
  elif player2=="R":
    print("player2's rock beats player1's scissors")
  elif player2=="S":
    print("its a draw! Play again.")
  else:
    print("Enter either R,P,or S")
else:
  print("Enter either R,P,or S")