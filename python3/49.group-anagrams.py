#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grouped_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            grouped_dict[sorted_word].append(word)

        grouped_list = list(grouped_dict.values())
        return grouped_list
    
# @lc code=end

