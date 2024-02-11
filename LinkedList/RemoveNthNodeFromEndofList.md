# [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

Given the head of a linked list, remove the nth node from the end of the list and return its head.

```py
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        count = 0

        iterate = head
        while iterate != None:
            count+=1
            iterate = iterate.next 

        count-=n
        prev = dummy
        for i in range(0 , count):
            prev = prev.next

        prev.next = prev.next.next
        return dummy.next
```