"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.
"""

#** Using Valley Peak Approach
def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    size = len(prices)
    profit = 0
    
    for i in range(1, size):
        # Check if the current price is higher than the previous price
        if prices[i] > prices[i-1]:
            # Add the difference between the current and previous price to the profit
            profit += prices[i] - prices[i-1]
            
    return profit 


#** Using Local Minimum and Local Maximum 
"""
A local minimum is a day when the stock price is lower than both the previous day and the next day.
A local maximum is a day when the stock price is higher than both the previous day and the next day.
The idea is to buy the stock at a local minimum and sell it at a local maximum, and repeat this process for all possible pairs of local minima and maxima.
"""
def maxProfit(prices):
    n = len(prices)
    profit = 0
    
    i = 0
    while i < n-1:
        # find the local minimum
        while i < n-1 and prices[i+1] <= prices[i]:
            i += 1
          
        # if we reach the end of the array, break the loop   
        if i == n-1:
            break
        
        # store the local minimum as the buying price
        buy = prices[i]
        
        i += 1
        
        # find the local maximum
        while i < n-1 and prices[i+1] >= prices[i]:
            i += 1
        
        # store the local maximum as the selling price    
        sell = prices[i]
        
        # update the profit
        profit +=  sell - buy
        
    return profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))
    print(maxProfit(prices)) # output = 7