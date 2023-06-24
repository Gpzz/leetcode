#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        answer = 0
        stack = []

        # Loop over list of bars
        for index, height in enumerate(heights):
            
            # Set relative start position variable to current index
            start = index

            # While new bar is taller than top element at top of stack
            while stack and stack[-1][1] > height:

                # Remove top of stack
                prev_index, prev_height = stack.pop()

                # Multiply prev height vs gap width between bars
                answer = max(answer, prev_height * (index - prev_index))

                # Update relative start position of new bar
                start = prev_index
            
            # Add new bar to stack with new relative start position
            stack.append([start, height])

        # For any remaining bars in stack check if they beat max answer
        for index, height in stack:
            answer = max(answer, height * (len(heights) - index))

        return answer

# @lc code=end

