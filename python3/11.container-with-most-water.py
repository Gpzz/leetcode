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

        # Set max_area to volume held by leftmost and rightmost bars
        max_area = min(height[left], height[right]) * (right - left)

        # Move pointers slowly together and check new area on each loop
        while left < right:
            # If new area is larger than the max area then update the max_area variable.
            current_area = min(height[left], height[right]) * (right - left)

            if current_area > max_area:
                max_area = current_area

            # We move the shortest of the two current bars inwards on each loop.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# @lc code=end

