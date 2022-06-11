months = ['j','f','m','a']
prices = [1,3,5,7,9,11,15]

min_price = min(prices)
print(min_price)

min_index = prices.index(min_price)
print(min_index)

min_month =months[min_index]
print(min_month)