#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Set a dummy node [0, Null] as a starting point for our linked list
        # We will use node to calculate the following nodes in our linked list
        dummy = node = ListNode()
        
        # Whilst either of the lists have nodes remaining
        while list1 and list2:

            # Take the smaller current node of the list
            if list1.val <= list2.val:
                # Set our linked list to point to the current smallest comparison node
                node.next = list1
                # Move list1 onwards to its next node
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            # Each time we grab a smallest value we move our linked list onwards to null
            node = node.next

        # Grab the remainder of the list that was not yet exhausted
        if list1:
            node.next = list1
        else:
            node.next = list2

        # Return dummy.next as this is the head of our linked list minus our original 
        # [0, Null] node that we created
        return dummy.next


# @lc code=end

