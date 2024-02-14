#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Sliding window problem.
        # For each distinct char in t the sliding window must contain at least the same amount as in t
        # This is tracked by t_count vs window_count

        res, left, right = "", 0, 0
        t_hashmap, window_hashmap = {}, {}

        # Counts of each character in t:
        for char in t:
            t_hashmap[char] = t_hashmap.get(char, 0) + 1

        t_count, window_count = len(t_hashmap), 0

        # Loop across length of s
        while right < len(s):

            # Rightmost character of the current sliding window
            right_char = s[right]

            # Include / Increment window hashmap value for right_char 
            window_hashmap[right_char] = window_hashmap.get(right_char, 0) + 1

            # If the inclusion / incrementation of right_char results in the sliding window containing the same amount
            # of the character as in t then we increment window_count by one to show that this character is satisfied
            if right_char in t and window_hashmap[right_char] == t_hashmap[right_char]:
                window_count += 1

            # Move sliding window inwards from the left until our condition is no longer met
            while t_count == window_count:

                # Leftmost character of the current sliding window
                left_char = s[left]

                # If res empty or new valid window is current shortest then update res
                if not bool(res) or right - left + 1 < len(res):
                    res = s[left:right+1]

                # We are going to remove the left_char from the sliding window. Therefore if they are currently equal they
                # soon wont be. We therefore decrement window_count as the condition is no longer met for this char in t.
                if left_char in t and window_hashmap[left_char] == t_hashmap[left_char]:
                    window_count -= 1

                # Remove leftmost character from sliding window
                window_hashmap[left_char] -= 1
                left += 1
            
            # Window has been reduced as much as possible for this endpoint, continue to extend window outwards on the right.
            right += 1

        return res

        
# @lc code=end

