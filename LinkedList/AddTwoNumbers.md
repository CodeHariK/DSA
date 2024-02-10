# [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

```py
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        rem = 0
        while l1 or l2 or rem:
            l1v = l1.val if l1 else 0
            l2v = l2.val if l2 else 0
            v = l1v + l2v + rem
            rem = v // 10
            r = v % 10
            curr.next = ListNode(r)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result.next
```