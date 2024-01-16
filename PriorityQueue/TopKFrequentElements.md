# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

## Go

```Go
func topKFrequent(nums []int, k int) []int {
    m := make(map[int]int)

    for _, num := range nums {
        m[num]++
    }

    queue := New[int, int64](MaxHeap)

    for key, value := range m {
        queue.Put(key, int64(value))
    }

    var ans []int

    for i := 0; i < k; i++ {
        item := queue.Get()
        ans = append(ans, item.Value)
    }

    return ans
}
```

## Java

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        
        Map<Integer,Integer> map = new HashMap();
        for(int n : nums){
            map.put(n,map.getOrDefault(n,0) + 1);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->map.get(b) - map.get(a));
        pq.addAll(map.keySet());

        int[] res = new int[k];
        for(int i = 0; i<k; i++){
            res[i] = pq.poll();
        }
        return res;
    }
}
```

## C++

```c++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        priority_queue<pair<int,int>> pq;

        for(int i: nums) mp[i]++;

        for(auto i: mp) {
            pq.push({i.second, i.first});
        }

        vector<int> res;

        while(k--) {
            res.push_back(pq.top().second);
            pq.pop();
        }

        return res;
    }
};
```

## Py

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        top_elements = heapq.nlargest(k, count, key=lambda i:count[i])
        return top_elements
```
