#Calculating the #of $20 and $10 in any amount
Dollars = int(input("Please Enter an amount of dollars for withdrawal: "))
Twenty = Dollars // 20
Dollars -= (Twenty * 20)
Ten = Dollars / 10
print ("The number of 10 dollar bills you will recieve is " + str(Ten))
print ("The number of 20 dollar bills you will recieve is " + str(Twenty))

