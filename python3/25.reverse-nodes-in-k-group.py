#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        # The node immediately preceeding the current group of k nodes
        # Initialised to dummy node for first group of k nodes
        group_prev = dummy

        while True:

            kth = self.getKthNode(group_prev, k)
            # If less than k elements remain then leave them untouched
            if not kth:
                break
            # The node immediately following the current group of k nodes
            group_next = kth.next

            # See 206.reverse-linked-list.py
            # https://github.com/Gpzz/leetcode/blob/main/python3/206.reverse-linked-list.py
            prev, curr = kth.next, group_prev.next
            
            while curr != group_next:

                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # group_prev was the first node of group and is the last node of reversed group
            # Momentarily store it in tmp
            tmp = group_prev.next
            # kth was the last node of group and is the first node of the reversed group
            group_prev.next = kth
            # Now update group_prev for next iteration to be at end of reversed group
            group_prev = tmp
            
        return dummy.next

    # Get kth node from linked list
    def getKthNode(self, curr, k):
        
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr


# @lc code=end

