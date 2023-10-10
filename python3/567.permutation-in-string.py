#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        from collections import Counter

        # Left and right pointers of len(s1) distance apart
        left, right = 0, len(s1)
        # Map of s1 character counts
        s1_map = Counter(s1)

        # Loop across all substrings in s2 of length s1.
        while right <= len(s2):

            # If character counts of s2 substring == s1 character counts then true
            if s1_map == Counter(s2[left:right]):
                return True

            # Increment pointers
            left += 1
            right += 1
        
        return False

# @lc code=end

