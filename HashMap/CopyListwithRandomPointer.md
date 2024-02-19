# [138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

```py
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = {None: None}
        
        curr = head
        while curr:
            ans[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            ans[curr].next = ans[curr.next]
            ans[curr].random = ans[curr.random]
            curr = curr.next
            
        return ans[head]
```