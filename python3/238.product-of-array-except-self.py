#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
from collections import Counter

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        number_counts = Counter(nums)
        answer = {}

        for index, number in enumerate(nums):
            product = 1
            number_counts[number] -= 1

            for key, value in number_counts.items():
                if value > 0:
                    product *= key ** value
                if value < 0:
                    product *= abs(key) ** value
                    product *= -1 * value

            answer[index] = product

            number_counts[number] += 1

        return answer.values()
# @lc code=end

