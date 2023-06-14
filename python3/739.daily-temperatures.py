#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)

        stack = [] # [index, temperature]

        for index, temperature in enumerate(temperatures):

            while stack and temperature > stack[-1][1]:

                stackindex, stacktemp = stack.pop()
                answer[stackindex] = index - stackindex
            
            stack.append([index, temperature])

        
        return answer
# @lc code=end

