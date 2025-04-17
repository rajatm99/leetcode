# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        h = href = head
        if head == None:
            return None
        head = head.next
        while head :
            if head.val == val:
                h.next = head.next
            else:
                h = head
            head = head.next
        if href.val == val:
            return href.next
        else :
            return href