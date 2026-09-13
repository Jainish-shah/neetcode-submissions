# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        count = 0
        while cur:
            count+=1
            cur = cur.next

        removeIndex = count - n
        cur = head
        counter = 0
        if removeIndex == 0:
            return head.next
            
        while cur:
            if removeIndex - 1 == counter:
                cur.next = cur.next.next
            cur = cur.next
            counter += 1
        return head
        