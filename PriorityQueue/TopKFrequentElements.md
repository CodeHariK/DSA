# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        res = []
        heap = []

        for val, freq in m.items():
            heapq.heappush(heap, (freq, val))
            if len(heap) > k:
                heapq.heappop(heap)
        while heap:
            _,val = heapq.heappop(heap)
            res.append(val)

        return res
```
