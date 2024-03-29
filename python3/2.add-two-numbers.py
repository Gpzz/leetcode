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
        pointer = res = ListNode(0)

        # While any remaining digits have not yet been added
        while l1 or l2 or carry:

            result = 0

            if l1:
                result += l1.val
                l1 = l1.next
            if l2:
                result += l2.val
                l2 = l2.next
            
            result += carry
            # Quotient is the carry variable
            carry = result // 10

            # Remainder is the current digit of the answer
            pointer.next = ListNode(result % 10)
            pointer = pointer.next

        return res.next
# @lc code=end

