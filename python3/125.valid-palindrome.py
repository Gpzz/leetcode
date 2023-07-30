#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:

        # Pointers to search through string from left and right
        left = 0
        right = len(s) - 1

        # Loop over sentence
        while left < right:

            # Work in from left and stop at each alpha-numeric char
            while left < right and not s[left].isalnum():
                left += 1
            # Work in from right and stop at each alpha-numeric char
            while right > left and not s[right].isalnum():
                right -= 1

            # If chars dont match then break with false
            if s[left].lower() != s[right].lower():
                return False
            
            # Continue to next char if more chars to consider
            left += 1
            right -= 1

        return True
            
# @lc code=end

