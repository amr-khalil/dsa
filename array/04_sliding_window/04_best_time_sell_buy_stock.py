"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    Time complexity: O(n)
    Space complexity: O(1)
    """
    max_profit = 0
    min_price = float('inf')
    for p in prices:
        min_price = min(min_price, p)
        profit = p - min_price
        max_profit = max(max_profit, profit)
        print(f"price: {p}, min_price: {min_price}, max_profit: {max_profit}")
    return max_profit

def maxProfit2(prices):
    """
    :type prices: List[int]
    :rtype: int
    Time complexity: O(n)
    Space complexity: O(1)
    """
    l, r = 0, 1
    max_profit = 0
    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        else:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        r += 1
    return max_profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit2(prices))  # 5
    prices = [7,6,4,3,1]
    print(maxProfit2(prices))  # 0
    prices = [7,6,4,3,1,8]
    print(maxProfit2(prices))  # 7
    prices = [7,6,4,3,1,8,10]

