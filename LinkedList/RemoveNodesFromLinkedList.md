# [2487. Remove Nodes From Linked List](https://leetcode.com/problems/remove-nodes-from-linked-list/description)

```py
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev,curr = None,node
            while curr:
                nxt = curr.next
                curr.next,prev,curr = prev,curr,nxt
            return prev

        dummy = ListNode()
        dummy.next = reverse(head)
        prev,curr = dummy,dummy.next

        while curr:
            if curr.val >= prev.val:
                prev.next = curr
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        return reverse(dummy.next)
```
