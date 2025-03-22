from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        r = dummy = ListNode()
        while list1 and list2 :
            if list1.val < list2.val :
                r.next = list1
                r = list1
                list1 = list1.next
            else:
                r.next = list2
                r = list2
                list2 = list2.next
            
        if list1 or list2:
            r.next = list1 if list1 else list2

        return dummy.next






# Create test lists
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Create Solution instance and call mergeTwoLists
solution = Solution()
result = solution.mergeTwoLists(list1, list2)

while result:
    print(result.val, end=" -> ")
    result = result.next

