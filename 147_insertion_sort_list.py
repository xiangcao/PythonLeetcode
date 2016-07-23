# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        prev = dummyHead
        cur = head.next
        head.next = None
        while cur:
            next = cur.next
            p = dummyHead.next
            prev = dummyHead
            while p and cur.val > p.val:
                prev = p
                p = p.next
            if p:
                prev.next = cur
                cur.next = p
            else:
                prev.next = cur
                cur.next = None
            cur = next
        return dummyHead.next
            
