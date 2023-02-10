print("hi im going to tell you your generation name")

year=int(input("what year were you born in?"))

if year>=1925 and year<=1946:
  print("you are called traditionalists!")
elif year>=1947 and year<=1964:
  print("you are the baby boomers")
elif year>=1965 and year<=1981:
  print("you are generation x")
elif year>=1982 and year<=1995:
  print("you are the millenials")
elif year>=1996 and year<=2015:
  print("you are generation z")
else:
    print("oops no name for you!")