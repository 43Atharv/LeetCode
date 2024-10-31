class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        curr = head.next
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head.next = None
        return prev