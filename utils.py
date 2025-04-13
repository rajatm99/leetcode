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