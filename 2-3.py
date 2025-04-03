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
		# get first number
		num_cx = 0
		num1 = 0
		node = l1
		while node is not None:
			num1 += node.val * (10**num_cx)
			num_cx += 1
			node = node.next

		# get second number
		num_cx = 0
		num2 = 0
		node = l2
		while node is not None:
			num2 += node.val * (10**num_cx)
			num_cx += 1
			node = node.next

		num_sum = num1 + num2
		output = ListNode(val=int(str(num_sum)[-1]))
		for digit in str(num_sum)[-2::-1]:
			node = output
			# traverse list to the end
			while node.next is not None:
				node = node.next
			node.next = ListNode(val=int(digit), next=None)

		return output


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
