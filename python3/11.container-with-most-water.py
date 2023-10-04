#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Set pointers to leftmost and rightmost bars
        left, right = 0, len(height) - 1

        # Initialize area variable
        area = 0

        # Move pointers slowly together and check new area on each loop
        while left < right:
            # If new area is larger than the current max area then update the area variable.
            area = max(area, min(height[left], height[right]) * (right - left))

            # We move the shortest of the two current bars inwards on each loop.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

# @lc code=end

