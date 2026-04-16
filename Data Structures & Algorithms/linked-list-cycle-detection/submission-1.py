# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited=set()
        while(head is not None):
            if(head.val not in visited):
                visited.add(head.val)
            else:
                if(head.next is not None):
                    return True
            head=head.next
        return False
    