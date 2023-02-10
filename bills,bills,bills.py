bill=float(input("what is the total bill?: "))
people=int(input("how many people: "))

tip_percentage=int(input("what % of tip?"))

tip=tip_percentage/100 * bill
total_amount=float(bill+tip)


print(round(total_amount,1),"is the total")
each=float(total_amount/people)


print("each person will pay",round(each,1),"dollars")