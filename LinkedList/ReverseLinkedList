# [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/description/)

Given the head of a singly linked list, reverse the list, and return the reversed list.

```py
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        n = head.next

        while n:
            nn = n.next
            n.next = p
            p = n
            n = nn

        return n
```
