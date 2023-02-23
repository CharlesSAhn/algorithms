


def findFraudulentTraders(datafeed):

	trades_map = {} #dict of day: price, name, transaction type, amount
	insiders = []
	price = -1

	for line in datafeed:
		entries = line.split("|")
		day = int(entries[0])

		if len(entries) == 2: #stock price increase/decrease
			price = int(entries[1])
			print(trades_map)

			for date in range(day - 3, day):
				if date in trades_map:
					for line in trades_map[date]:
						[prev_price, trader_name, transaction, amount] = line

						if transaction == "BUY":
							profit = (price - prev_price) * amount
						else: #SELL
							profit = (prev_price - price) * amount

						if profit >= 5000000:
							insiders.append((date, trader_name))
		else:
			if day not in trades_map:
				trades_map[day] = []

			name = entries[1]
			transaction = entries[2]
			amt = entries[3]

			#keep track of price on that day along with name, transaction type, amount bought/sold
			trades_map[day].append((price, name, transaction, int(amt))) 

	insiders = set(sorted(insiders))
	#print(trades)

	
	#reformatting answer to list of day|name
	ans = []
	for entry in insiders:
		day = entry[0]
		name = entry[1]
		concat = str(day) + "|" + name
		ans.append(concat)


	return list(map(lambda x: str(x[0]) + "|" + str(x[1]), insiders))



#Detect 'insider trading' based on string input of stock price, users' buy/sell data for some range of days.
#If profit made or loss prevented is greater that the given value, that trade is considered an insider trade.  

feed1 = """0|1000
0|Shilpa|BUY|30000
0|Will|BUY|50000
0|Tom|BUY|40000
0|Kristi|BUY|15000
1|Kristi|BUY|11000
1|Tom|BUY|1000
1|Will|BUY|19000
1|Shilpa|BUY|25000
2|1500
2|Will|SELL|7000
2|Shilpa|SELL|8000
2|Kristi|SELL|6000
2|Tom|SELL|9000
3|500
38|1000
78|Shilpa|BUY|30000
79|Kristi|BUY|60000
80|1100
81|1200"""

datafeed1 = feed1.split("\n")
print(findFraudulentTraders(datafeed1))
