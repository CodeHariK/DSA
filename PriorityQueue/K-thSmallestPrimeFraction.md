# [786. K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction)

```py
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)
        for i in range(n-1):
            heappush(heap,(arr[i]/arr[-1],i,n-1))
            # print(heap)
        
        for i in range(k-1):
            res,l,r = heappop(heap)
            # print('---')
            # print((l,r))
            heappush(heap,(arr[l]/arr[r-1],l,r-1))
            # print((l,r-1))

        res,l,r = heappop(heap)

        return [arr[l],arr[r]]
```
