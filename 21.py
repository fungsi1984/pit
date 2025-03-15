from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Standalone function to represent a linked list as a string
def listnode_to_string(node: Optional[ListNode]) -> str:
    result = []
    current = node
    while current:
        result.append(str(current.val))
        current = current.next
    return " -> ".join(result)


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2
        if list1.val > list2.val:
            list1, list2 = list2, list1
        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1


# Example usage
if __name__ == "__main__":
    # Create two sorted linked lists
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6])

    # Print the original lists
    print("List 1:", listnode_to_string(list1))
    print("List 2:", listnode_to_string(list2))

    # Merge the two lists
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)

    # Print the merged list
    print("Merged List:", listnode_to_string(merged_list))
