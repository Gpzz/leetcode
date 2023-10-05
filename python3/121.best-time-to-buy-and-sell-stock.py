#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Initialise profit tracking variable and left, right pointers
        max_profit = 0
        left, right = 0, 1
        
        # Move right (sell) over until all prices are tested
        while right < len(prices):

            profit = prices[right] - prices[left]

            # Update profit tracker if new max profit is found
            max_profit = max(max_profit, profit)

            # If making a loss we can skip left pointer to the right pointer
            if profit < 0:
                left = right

            right +=1

        return max_profit
        
# @lc code=end

