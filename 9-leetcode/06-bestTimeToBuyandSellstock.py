'''
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


'''

def solution(prices):
    slow = 0
    fast = 1
    maxP = 0

    while fast < len(prices):
        if prices[slow] < prices[fast]:
            profit = prices[fast] - prices[slow]
            # max(something, something) we can compare 2 which one is bigger
            maxP = max(maxP, profit)
        else:
            slow = fast
        fast += 1

    return maxP







print(solution([7,1,5,3,6,4]))
print(solution([7,6,4,3,1]))