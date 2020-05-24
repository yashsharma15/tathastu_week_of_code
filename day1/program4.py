cp = int(input("Cost Prise :"))
sp = int(input("Selling Prise :"))
profit = sp - cp
new_profit = ((5/100) * profit) + profit
new_sp = cp + new_profit
print(profit)
print(new_sp)
