from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = ListNode()
        carry = 0
        while l1 and l2:
            s = l1.val + l2.val + carry
            print("1 - ", s)
            result.next = ListNode(s%10)
            carry = s//10
            l1 = l1.next
            l2=l2.next
            result = result.next
        
        while l1:
            s = l1.val + carry
            print("2 - ", s)
            result.next = ListNode(s%10)
            carry = s//10
            l1 = l1.next
            result = result.next

        while l2:        
            s = l2.val + carry
            print("3 - ", s)
            result.next = ListNode(s%10)
            carry = s//10
            l2= l2.next
            result = result.next

        if carry != 0 :
            result.next = ListNode(carry)

        return head.next
        
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Create Solution instance and call mergeTwoLists
solution = Solution()
result = solution.addTwoNumbers(list1, list2)

# Print the result (optional)
while result:
    print(result.val, end=" -> ")
    result = result.next