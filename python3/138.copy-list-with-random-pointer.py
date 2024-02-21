#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # Initialise pointer and hashmap
        # Requires None:None for when curr.next = None we want to return None
        curr = head
        hashmap = {None:None}

        # First pass through linked list
        while curr:
            # Add each node to hashmap - only .val is set
            copy = Node(curr.val)
            hashmap[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            # Get the .val value and set .next and .random of copied nodes
            # using .next and .random of original nodes
            copy = hashmap[curr]
            copy.next = hashmap[curr.next]
            copy.random = hashmap[curr.random]
            curr = curr.next
        
        # head of copied nodes is stored in the hashmap
        return hashmap[head]


# @lc code=end

