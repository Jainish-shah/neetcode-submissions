# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = self.merge2Lists(lists[i-1], lists[i])
        
        return lists[-1]
    

    def merge2Lists(self, l1, l2) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

        
        
        
        
        
        # nodes = []
        # for l in lists:
        #     while l:
        #         nodes.append(l.val)
        #         l = l.next
        # nodes.sort()
        # res = ListNode(0)
        # cur = res
        # for node in nodes:
        #     cur.next = ListNode(node)
        #     cur= cur.next
        # return res.next