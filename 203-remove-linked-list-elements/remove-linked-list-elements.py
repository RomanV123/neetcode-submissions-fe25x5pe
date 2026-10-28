# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:


        if head is None:
            return head
        

# first, remove matching nodes from the front
        while head is not None and head.val == val:
            head = head.next

# then traverse the remaining list
        current = head

        while current is not None and current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return head 

            