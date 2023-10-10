#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Hashmap of character counts in substring
        letter_map = {}
        left = max_replacement = res = 0

        # Loop across entire string
        for right in range(len(s)):

            # Add or increment letter count in hashmap
            if s[right] in letter_map:
                letter_map[s[right]] += 1
            else:
                letter_map[s[right]] = 1

            # If newest letter is new maximum count then update max_replacement
            max_replacement = max(max_replacement, letter_map[s[right]])

            # If more than k replacements required then move left pointer right a step
            if right - left + 1 - max_replacement > k:
                letter_map[s[left]] -= 1
                left += 1
            
            # Update res if new max length substring found
            res = max(res, right - left + 1)

        return res
        
# @lc code=end

