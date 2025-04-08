from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        trav = head
        l = 0
        while trav.next != None:
            l += 1
            trav = trav.next
        print(l)
        l += 1
        if l == 1:
            print(" l = 1")
            return None
        trav = head
        for i in range((l // 2) -1):
            trav = trav.next
        
        trav.next = trav.next.next
        return head


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
arr = [1]
head = create_linked_list(arr)
print("Original list:")
print_linked_list(head)

sol = Solution()
new_head = sol.deleteMiddle(head)

print("After deleting middle:")
print_linked_list(new_head)