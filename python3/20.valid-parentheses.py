#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        
        open_brackets = []
        bracket_pairs = { ")": "(", "}": "{", "]": "["}

        for character in s:

            if character not in bracket_pairs: # Open bracket that needs adding
                open_brackets.append(character)
                continue

            if open_brackets and open_brackets[-1] == bracket_pairs[character]: # Matching closed bracket
                open_brackets.pop()
                continue

            return False

        if open_brackets: # Check for remaining unclosed open brackets
            return False
        
        return True
      
# @lc code=end

