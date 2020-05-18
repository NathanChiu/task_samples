# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd(self, head, n):
        # node_delete = None
        node = head
        node_delete = head
        i = 0
        while node.next:
            node = node.next
            if i >= n-1:
                node_delete = node_delete.next
            i += 1
        if node_delete.next:
            node_delete.val = node_delete.next.val
            node_delete.next = node_delete.next.next
        else:
            return []
        return head
