class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        main = None
        minor - None
        if l1.val > l2.val:
            main = l2
            minor = l1
        else:
            main = l1
            minor = l2
        
        ptr = main
        while minor:
            if ptr.next and ptr.next.val > minor.val:
                tmp = minor.next
                minor.next = ptr.next
                ptr.next = minor
                minor = tmp
            else if ptr.next is None:
                ptr.next = minor
                break
            else:
               ptr = ptr.next
        
        return main
