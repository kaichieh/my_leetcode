class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        fast = slow = head
        for x in range(n):
            if fast:
                fast = fast.next
        if fast is None:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        
        return head
