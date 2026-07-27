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
        mapping = {}
        ptr = head
        while ptr != None:
            mapping[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head
        while ptr != None:
            copy_ptr = mapping.get(ptr)
            copy_next = mapping.get(ptr.next)
            copy_ptr.next = copy_next
            if ptr.random:
                copy_random = mapping.get(ptr.random)
                copy_ptr.random = copy_random
            ptr = ptr.next
        
        return mapping.get(head)
        