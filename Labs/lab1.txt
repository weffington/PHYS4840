max_money = float(input('enter amount of money: '))
cookieNames = ["Sugar", "Chocolate", "Snickerdoodle", "S'mores"]
cookiePrices = [2.65, 3.20, 3.45, 3.70]
for i in range(0,4):
	canBuy = max_money//cookiePrices[i]
	cookieNumber = max_money%cookiePrices[i]
	if canBuy == 0:
		print(f"Can buy 0 {cookieNames[i]} cookies")
		break
	else:
		print(f"Can buy {round(canBuy,0)} {cookieNames[i]} with ${round(cookieNumber,3)} in change.")
