# [2816. Double a Number Represented as a Linked List](https://leetcode.com/problems/double-a-number-represented-as-a-linked-list)

```py
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def rev(h):
            pre, cur = None, h
            while cur:
                nxt = cur.next
                pre, cur.next, cur = cur, pre, cur.next
            return pre
        r = rev(head)
        ans = r

        c = 0
        while r:
            d = c + r.val * 2
            c = d // 10
            r.val = d % 10

            if c != 0 and r.next is None:
                r.next = ListNode(val=c)
                break
            r = r.next
        return rev(ans)
```
