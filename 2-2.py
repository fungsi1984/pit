from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(
		self, l1: Optional[ListNode], l2: Optional[ListNode]
	) -> Optional[ListNode]:
		dummy_head = ListNode(0)
		current = dummy_head
		carry = 0

		while l1 or l2 or carry:
			val1 = l1.val if l1 else 0
			val2 = l2.val if l2 else 0

			sum_val = val1 + val2 + carry
			carry = sum_val // 10
			current.next = ListNode(sum_val % 10)
			current = current.next

			if l1:
				l1 = l1.next
			if l2:
				l2 = l2.next

		return dummy_head.next


def to_linked_list(arr):
	if not arr:
		return None
	head = ListNode(arr[0])
	current = head
	for val in arr[1:]:
		current.next = ListNode(val)
		current = current.next
	return head


def to_list(head):
	result = []
	current = head
	while current:
		result.append(current.val)
		current = current.next
	return result


def main():
	l1 = to_linked_list([2, 4, 3])
	l2 = to_linked_list([5, 6, 4])
	solution = Solution()
	result = solution.addTwoNumbers(l1, l2)
	print(to_list(result))  # Output: [7, 0, 8]

if __name__ == "__main__":
    main()