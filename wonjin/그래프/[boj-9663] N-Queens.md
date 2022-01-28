# [boj-9663] N-Queens [python]

## [문제](https://www.acmicpc.net/problem/9663) 

## 의사코드
- 시간초과 발생할 수 있음


### py code
```py
import sys
input = sys.stdin.readline

def check(n):
    for i in range(n):
        if row[n] == row[i] or abs(row[n]-row[i]) == n-i:
            return 0
    return 1
        
def dfs(n):
    global res
    if n == N:
        res += 1
    else:
        for i in range(N):
            row[n] = i
            if check(n):
                dfs(n+1)

N = int(input())
row = [0]*15
res = 0
dfs(0)
print(res)
```
