# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next

        length = count - n
        if length == 0:
            return head.next

        temp = head
        for i in range(count-1):
            if (i + 1) == length:
                temp.next = temp.next.next
                break
            temp = temp.next       
        return head

