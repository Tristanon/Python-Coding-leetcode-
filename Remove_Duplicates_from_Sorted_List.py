# Remove_Duplicates_from_Sorted_List.py
# Solution 1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        previous_node = ListNode(head)
        seen=set()
        while current_node:
            if current_node.val in seen:
                previous_node.next = current_node.next
                current_node.next = None
                current_node = previous_node.next
            else:
                seen.add(current_node.val)
                previous_node = current_node
                current_node = current_node.next
        return head