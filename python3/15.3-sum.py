#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         
        res = []
        nums.sort() # Create an ordered array to use two sum ii approach

        for index, a in enumerate(nums):

            # Array pointers at ends of list
            left, right = index + 1, len(nums) - 1

            while left < right:

                b, c = nums[left], nums[right]

                # If current sum is greater than 0 move right pointer inwards & vice versa
                if a + b + c > 0:
                    right -= 1
                elif a + b + c < 0:
                    left += 1
                else:
                    # If the result is unique then add it to the results
                    if [a,b,c] not in res:
                        res.append([a,b,c])
                    # Move a pointer across to prevent continuous loop
                    left += 1
            
        return res # [-2,0,1,1,2]

# @lc code=end

