# Input: prices = [7,1,5,3,6,4]
# Output: 5
def MaxProfit(prices):
    min_price = float('inf') # 初始為正無窮大
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price  # Update min_price if current price is lower
        elif price - min_price > max_profit:
            max_profit = price - min_price  # Update max_profit if current profit is higher
    return max_profit


print(MaxProfit([7,1,5,3,6,4]))