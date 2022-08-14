prices = [1,6,4,3,1,9]
minprice = prices[0]
maximumprofit = 0
for i in prices[1:]:
	profit = i - minprice
	maximumprofit = max(maximumprofit,profit)
	minprice = min(minprice,i)
print(maximumprofit)