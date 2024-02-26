#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Floyd's algorithm
        fast = slow = 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                slow = 0
                break

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast

# @lc code=end
