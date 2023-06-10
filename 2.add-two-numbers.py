#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        answer = ListNode(0)
        pointer = answer

        while l1 or l2 or carry:

            result = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = result // 10
            
            pointer.next = ListNode(result % 10)
            pointer = pointer.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return answer.next
# @lc code=end

