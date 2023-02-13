print("****finding the number of seconds in a year****")
seconds=60
minutes=60
hours=24

year=int(input("enter the year:"))
if (year%400) ==0 or (year%100) ==0 or (year%4) ==0 :
  print("the number of seconds is",366*hours*minutes*seconds)
else:
  print("the number of seconds is",365*hours*minutes*seconds)