from random import randint

name = input("Enter name : ")
income = int(input("Enter your total income or savings : "))
amount = int(input("Enter maximum amount you can invest : "))
while income < amount:
  print("Your investment amount can not be more than your savings.")
  amount = int(input("Enter maximum amount you can invest : "))

print(f"\nHi! {name} welcome to VedStocks \nCheckout leaderboard for stock's information\n")

#upper and lower limit of stock values 
stocks_range = {"RIL":[1000,4000], "L&T":[2000,3000], "TATA":[1000,2000], "Wipro":[3000,6000], "IBM":[2500,3500], 
          "Google":[4000,5000], "Apple":[1000,3000], "TCS":[4000,7000], "Tinder":[1000,3000], "Infosys":[5000,7000]}

stocks_range_copy = {"RIL":[1000,4000], "L&T":[2000,3000], "TATA":[1000,2000], "Wipro":[3000,6000], "IBM":[2500,3500], 
          "Google":[4000,5000], "Apple":[1000,3000], "TCS":[4000,7000], "Tinder":[1000,3000], "Infosys":[5000,7000]}

#to decide base values of stock
base_stocks = stocks_range
for i in base_stocks:
  base_stocks[i] = randint(stocks_range[i][0],stocks_range[i][1])

#to store variable values of stocks  
stocks = stocks_range_copy
for i in stocks:
  stocks[i] = randint(stocks_range_copy[i][0],stocks_range_copy[i][1])

print('*'*50+'\n**\t\tStock Market Leaderboard\t**\n'+'*'*50+'\nStock\t\tStart Price\tCurrent Price')

for i in stocks:
  if randint(1,10) < 5:
    stocks[i] = stocks[i] - float(stocks[i]*0.30)
  elif randint(1,10) > 5:
    stocks[i] = stocks[i] + float(stocks[i]*0.30) 

for i in stocks:
  print(f"{i}\t\t{base_stocks[i]}\t\t{stocks[i]}")
  
print('*'*50)  

stock_option = input("Enter stock which you want to buy : ")
maximum_no_of_stocks = amount // int(stocks[stock_option])
print(f"You can by maximum '{maximum_no_of_stocks}' stocks from '{stock_option}'")

no_of_stocks_brought = int(input("How many stocks you want to buy ? "))
while no_of_stocks_brought > maximum_no_of_stocks:
	print("You can not exceed your buy limit")
	no_of_stocks_brought = int(input("How many stocks you want to buy ? "))

invested_amount = int(stocks[stock_option]) * no_of_stocks_brought
remaining_amount = amount - invested_amount
print(f"\nYou have only Rs. {remaining_amount} remaining as your investment amount")
print(f"\nYour stock details:")

base_value = int(base_stocks[stock_option])
current_value = int(stocks[stock_option])

if base_value < current_value:
	profit = (current_value - base_value) * 100 / current_value
	loss = 0
else:
	profit = 0
	loss = (base_value - current_value) * 100 / current_value

my_stocks = {"name":stock_option, "quantity":no_of_stocks_brought, "buy_value":base_value, "current_value":current_value, "profit":profit, "loss":loss}

print("\nName\tQuantity\tBuy Value\tCurrent Value\tProfit\tLoss")

for i in my_stocks:
	print(my_stocks[i],end="\t")



	
