# Input: prices = [7,1,5,3,6,4]
# Output: 5
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j]-prices[i] > max_profit:
                max_profit = prices[j]-prices[i]
            
    return max_profit

print(maxProfit([7,6,4,3,1]))

        