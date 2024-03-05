# [2013. Detect Squares](https://leetcode.com/problems/detect-squares/description/)

You are given a stream of points on the X-Y plane. Design an algorithm that:

Adds new points from the stream into a data structure. Duplicate points are allowed and should be treated as different points.
Given a query point, counts the number of ways to choose three points from the data structure such that the three points and the query point form an axis-aligned square with positive area.
An axis-aligned square is a square whose edges are all the same length and are either parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

DetectSquares() Initializes the object with an empty data structure.
void add(int[] point) Adds a new point point = [x, y] to the data structure.
int count(int[] point) Counts the number of ways to form axis-aligned squares with point point = [x, y] as described above.

```py
class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for (x, y), n in self.ptsCount.items():
            if (abs(px - x) == abs(py - y)) and abs(px - x) > 0:
                res += n * self.ptsCount.get((px, y), 0) * self.ptsCount.get((x, py), 0)
        return res
```
