# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nums = []
        cur = head
        while cur:
            nums.append(cur)
            cur = cur.next
        
        removeIdx = len(nums) - n
        if removeIdx == 0:
            return head.next
        
        nums[removeIdx - 1].next = nums[removeIdx].next

        return head