#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:

        # Initialise boundary height variables
        max_left = max_right = 0
        # Initialise boundary left and right pointers
        left, right = 0, len(height) - 1
        area = 0

        # Move the pointers closer together
        while left < right:

            # Set the boundary height variables to the largest height seen
            max_left = max(max_left, height[left])
            max_right = max(max_right, height[right])

            # Move the smaller of the two boundary pointers inwards
            if height[left] < height[right]:
                left += 1
                area += max(0, max_left - height[left])
            else:
                right -= 1
                area += max(0, max_right - height[right])
            
        return area

# @lc code=end

