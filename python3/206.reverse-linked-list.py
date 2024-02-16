#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Initialise two pointers (One node before head and head)
        prev, curr = None, head

        # Curr will only be None once the end of the linked list has been reached
        while curr:
            # Temp save pointer location of current node
            temp = curr.next
            # Reverse the pointer of current node
            curr.next = prev
            # Move our pointer up a node
            prev = curr
            # Move our second pointer up a node
            curr = temp
        # Return the head of the reversed linked list
        return prev

# @lc code=end

