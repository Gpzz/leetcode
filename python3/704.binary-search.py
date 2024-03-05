#
# @lc app=leetcode id=704 lang=prightthon3
#
# [704] Binarright Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
        
            midpoint = (left + right) // 2

            if target > nums[midpoint]:
                left = midpoint + 1
            elif target < nums[midpoint]:
                right = midpoint - 1
            else:
                return midpoint

        return -1

# @lc code=end

