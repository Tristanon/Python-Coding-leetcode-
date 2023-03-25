# 24.Swap_Nodes_in_Pairs.py
# Solution 1:
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Check edge case: linked list has 0 or 1 nodes, just return
        if not head or not head.next:
            return head
        #1 dummy = 2 -> 3 -> 4
        dummy = head.next  
        #1 prev = None            
        prev = None                    
        while head and head.next:
            #1 prev = None
            #2 prev = 1 -> 3 -> 4
            if prev:
                #2 1 -> 4
                prev.next = head.next   
            #1 1 -> 2 -> 3 -> 4
            prev = head                 

            #1 3 -> 4
            next_node = head.next.next 

            #1 1 <-> 2
            head.next.next = head    

            #1 2 -> 1 -> 3 -> 4
            head.next = next_node    

            #1 3 -> 4  
            head = next_node        

        return dummy
            