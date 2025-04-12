from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = 0
        h = head
        while h:
            n += 1
            h = h.next

        i = 0
        h = head
        while i < n/2:
            h = h.next
            i += 1    

        tail = self.reverse(h)   
        max = -100000

        i = 0
        while i < n/2:
            sum = head.val + tail.val
            print("sum", sum)
            if max < sum:
                max = sum    
            i += 1
            head = head.next
            tail = tail.next

        print(max)

        print(n)
        print_linked_list(head)
        print_linked_list(tail)
        return max

    def reverse(self, head) -> ListNode:
        h1 = head
        h2 = head.next
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
arr = [47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
head = create_linked_list(arr)
print("Original list:")
print_linked_list(head)

sol = Solution()
print(sol.pairSum(head))

