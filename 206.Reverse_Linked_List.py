# 206.Reverse_Linked_List.py
# Solution1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        # 1->2->3->4->5
        
        while current:
            dummy = current.next
            # 3 -> 4 -> 5
            current.next = previous
            # None <- 1 <- 2
            previous = current
            # previous = 1 -> None
            # previous = 2 -> 1 -> None
            current = dummy
            # current = 2 -> 3 -> 4 -> 5
            # current = 3 -> 4 -> 5
        
        return previous