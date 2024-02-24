# [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description)

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

```py
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra's with minHeap -- O(E + n * logn)
            # n = num of nodes
            # minHeap can have at most n elements (edges from src to every other nodes)
            # at a time -- each pop, push ops take logn
            # E for building graph
        # the idea is to keep track of visited nodes with visited array
        # visited[i] = steps it took to reach i from src
        # at each iteration, if curr steps < visited[i], continue explore that path
        # even if the cost is higher -- in case prev/cheaper path doesn't reach
        # target in valid number of steps

        graph = defaultdict(dict)
        for u, v, w in flights:
            graph[u][v] = w
        minHeap = [(0, src, 0)] # (cost, curr node, steps from src)
        visited = [float('inf')] * n

        while minHeap:
            currCost, currNode, currSteps = heapq.heappop(minHeap)
            if currNode == dst:
                return currCost
            if currSteps > k or currSteps >= visited[currNode]:
                continue
            visited[currNode] = currSteps

            for neighbor, price in graph[currNode].items():
                heapq.heappush(minHeap, (currCost + price, neighbor, currSteps + 1))
        
        return -1
```