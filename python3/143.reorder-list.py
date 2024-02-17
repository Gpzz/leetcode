#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # 2 Pointers - slow is at midpoint when fast is at end
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Shift over the midpoint by one node
        second = slow.next
        # Set a reverse node to Null - will end up as head of reversed list
        # Set slow.next to None to prevent cycling between first and second half of list once reversed.
        reverse = slow.next = None
        
        # Reverse the second half of the list
        while second:
            dummy = second.next
            second.next = reverse
            reverse = second
            second = dummy

        # Splice the two lists together
        while reverse:
            # Use two placeholders for next nodes as links will be severed
            head_next, reverse_next = head.next, reverse.next
            head.next = reverse
            reverse.next = head_next
            head, reverse = head_next, reverse_next

        
# @lc code=end

