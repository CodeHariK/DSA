# [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/description/)

Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse(node):
            curr,prev = node,None
            while curr:
                curr.next,prev,curr = prev,curr,curr.next
            return prev

        dummy = ListNode()
        dummy.next = head
        slow,fast = dummy,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        temp = reverse(slow.next)
        slow.next = None

        while temp and head and temp.val == head.val:
            temp=temp.next
            head=head.next

        return not temp or not head
```
