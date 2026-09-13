"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        cur = head
        while cur:
            copy = Node(cur.val)
            self.map[cur] = copy
            cur = cur.next

        cur = head
        while cur:
            copy = self.map[cur]
            copy.next = self.map.get(cur.next)
            copy.random = self.map.get(cur.random)
            cur = cur.next
        return self.map[head]