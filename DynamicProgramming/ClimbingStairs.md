# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Go

```Go
func climbStairs(n int) int {
    if n == 0 || n == 1 {
        return 1
    }

    a, b := 1, 1
    var c int

    for i := 2; i <= n; i++ {
        c = a + b
        a, b = b, c
    }

    return c
}
```

## Java

```java
class Solution {
    public int climbStairs(int n) {
        if(n==0 || n==1) return 1;
        int a=1,b=1;
        int c = 0;
        for(int i=2;i<=n;i++){
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }
}
```

## C++

```c++
class Solution {
public:
    int climbStairs(int n) {
        if(n==0 || n==1) return 1;
        int a=1,b=1;
        int c;
        for(int i=2;i<=n;i++){
            c=a+b;
            a=b;
            b=c;
        }
        return c;
    }
};
```

## Py

```py
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        a,b = 1,2
        for i in range(2,n-1):
            a,b = b, a + b
        return a + b
```
