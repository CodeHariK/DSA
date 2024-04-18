# [621. Task Scheduler](https://leetcode.com/problems/task-scheduler/description/)

```py
class Solution:
    from collections import Counter
    def leastInterval(self, tasks: List[str], n: int) -> int:

        task_count = Counter(tasks)
        counts = [-task_count[task] for task in task_count]
        heapq.heapify(counts)
        idx, intervals, last = 0, 0, 0

        used = []
        intervals = 0
        while counts:
            count = 0
            for i in range(n+1):
                print(counts, count, intervals)
                if not counts and used:
                    intervals += n - i + 1
                    break
                elif not counts: break
                if counts[0] == -1:
                    heapq.heappop(counts)
                else:
                    used.append(heapq.heappop(counts))
                    used[-1] += 1
                intervals += 1
            counts += used
            used, count = [], 0
            print(intervals)
        
        return intervals
```
