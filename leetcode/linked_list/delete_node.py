# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #turn this node val into next node val.
        node.val = node.next.val
        #set next to next next, leaving no node to point to current next.
        node.next = node.next.next
# sol = Solution()
