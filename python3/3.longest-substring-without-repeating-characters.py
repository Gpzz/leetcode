#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Set two pointers to first and second position in string
        left = 0
        max_length = 0
        # Initialise set to track index of letters in current substring
        letters = set()

        # Loop across entire sequence of letters
        for right in range(len(s)):

            # If current letter is already in substring
            # 1. Move left across
            # 2. Update the set in accordance with the new substring
            while s[right] in letters:
                letters.remove(s[left])
                left += 1

            # Add the newest letter at the right pointer to the substring
            letters.add(s[right])
            
            # Update the max length variable if new substring > previous max
            max_length = max(max_length, right - left + 1)

        return max_length

# @lc code=end

