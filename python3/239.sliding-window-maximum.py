#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # Double ended queue
        from collections import deque

        # Stack holds the relevant values in each sliding window
        # Res holds the max value in each sliding window
        stack, res = deque(), []

        # Loop across nums
        for i, number in enumerate(nums):

            # Remove any elements of stack that are no longer in sliding window
            while stack and stack[0] < i - k + 1:
                stack.popleft()

            # Remove redundant elements from top of stack.
            while stack and number > nums[stack[-1]]:
                stack.pop()

            # Append number in index i of nums to top of stack
            stack.append(i)

            # This condition allows us to initialise the stack for 0<i<k in the same loop
            # without affecting res.
            if i >= k - 1:
                res.append(nums[stack[0]])

        return res
        

# @lc code=end

