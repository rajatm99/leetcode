# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        e = even
        o = odd

        if head == None:
            return head

        i = 2
        odd.next = ListNode(head.val)
        odd = odd.next
        head = head.next
        while head != None:
            if i % 2 == 0:
                even.next = ListNode(head.val)
                even = even.next
            else :
                odd.next =  ListNode(head.val)
                odd = odd.next
            i += 1
            head = head.next
        odd.next = e.next
        return o.next
        



def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=' -> ' if current.next else '\n')
        current = current.next

# Test the deleteMiddle function
arr = [1,2,3,4,5,6,7,8,9]
head = create_linked_list(arr)
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.oddEvenList(head)

print("After deleting middle:")
print_linked_list(new_head)