def login():
  while True:
    username=input("enter your username: ")
    password=int(input("enter passsword: "))
    if username=="tee" and password==1234:
      print("Welcome to Replit")
      break
    else:
      print("Whoops! I dont recognize that username or password. Try again!")
      continue

login()
    