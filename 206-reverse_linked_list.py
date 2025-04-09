# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        h1 = head
        h2 = head.next

        if h2 == None:
            return h1

        head = head.next.next
        h1.next = None
        while head:
            h2.next = h1
            h1 = h2
            h2 = head
            head = head.next
        
        h2.next = h1
        return h2

        
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
arr = [1,2,3]
head = create_linked_list(arr)
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.reverseList(head)

print("After deleting middle:")
print_linked_list(new_head)