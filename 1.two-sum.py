#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        checked_numbers = {}

        for index, number in enumerate(nums):

            if target - number in checked_numbers:
                return [checked_numbers[target - number], index]
            else:
                checked_numbers[number] = index

# @lc code=end

