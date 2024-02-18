#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # dummy node required for input: [1]\n1
        res = node = ListNode(None, head)
        loop = 0

        # Loop across entire linked list
        while head:
            head = head.next
            loop += 1

            # Secondary loop initiates after n iterations starting from dummy node
            if loop > n:
                node = node.next
            
        # Skip the nth node by updating pointer of n-1th node to point at n+1th node
        node.next = node.next.next

        return res.next
        

# @lc code=end

