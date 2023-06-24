#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse = True)
        stack = []
        answer = 0

        for car in cars:
            
            steps = (target - car[0]) / car[1]

            if not stack:
                stack.append(steps)
                answer += 1
                continue

            if steps > stack[-1]:
                stack.pop()
                stack.append(steps)
                answer += 1

        return answer
# @lc code=end

