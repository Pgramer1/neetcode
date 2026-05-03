# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for node in lists:
            while node:
                nodes.append(node.val)
                node = node.next
        nodes.sort()

        head = ListNode(0)
        dummy = head
        for node in nodes:
            dummy.next = ListNode(node)
            dummy = dummy.next

        return head.next