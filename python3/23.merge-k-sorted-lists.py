#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        while len(lists) > 1:

            merged = []

            # Merge two lists at a time
            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if len(lists) > i + 1 else None
                merged.append(self.mergeLists(l1, l2))

            # Update list of lists to be list of new merged lists
            # Essentially the number of lists is halved
            lists = merged
        
        return lists[0]
        
    # See 21.Merge-two-sorted-lists.py
    # https://github.com/Gpzz/leetcode/blob/main/python3/21.merge-two-sorted-lists.py
    def mergeLists(self, l1: List, l2: List):

        dummy = node = ListNode()

        while l1 and l2:

            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1
        else:
            node.next = l2

        return dummy.next
# @lc code=end
    
    #[[1,4,5],[1,3,4]]

