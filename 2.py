# Definition for singly-linked list node
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify the result list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Continue while there are digits to process or a carry exists
        while l1 or l2 or carry:
            # Get values if nodes exist, otherwise use 0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum and new carry
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            # Create new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes if they exist
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# Example usage:
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    current = head
    while current:
        values.append(str(current.val))
        current = current.next
    return " -> ".join(values)


# Test the solution
solution = Solution()

# Example: 342 + 465 = 807
l1 = create_linked_list([2, 4, 3])  # represents 342 (digits in reverse order)
l2 = create_linked_list([5, 6, 4])  # represents 465 (digits in reverse order)
result = solution.addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: 7 -> 0 -> 8

# Example: 999 + 1 = 1000
l1 = create_linked_list([9, 9, 9])  # represents 999
l2 = create_linked_list([1])  # represents 1
result = solution.addTwoNumbers(l1, l2)
print(print_linked_list(result))  # Output: 0 -> 0 -> 0 -> 1
