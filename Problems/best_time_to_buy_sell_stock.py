"""
Maximize the profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
"""

# Brute Force Method
def max_profit_brute(prices):
    profit = 0
    size = len(prices)
    
    for i in range(size):
        for j in range(i+1, size):
            if prices[j] > prices[i]:
                curr_profit = prices[j] - prices[i]
                if curr_profit > profit:    
                    profit = curr_profit
    return profit


#** Keep track of the minimum price and the maximum profit so far. 
def max_profit(prices):
    min_element = prices[0]
    profit = 0
    
    for price in prices:
        if price < min_element:
            min_element = price
        elif price - min_element > profit:
            profit = price - min_element
            
    return profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    print(max_profit(prices))
    print(max_profit_brute(prices)) # output = 5