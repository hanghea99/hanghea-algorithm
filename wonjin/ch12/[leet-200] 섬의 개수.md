# Number of Islands [python]

## [문제](https://leetcode.com/problems/number-of-islands/) 

## 의사코드
1. 그래프를 인접 행렬로 나타내었다. 이중 배열을 모두 돌면서 상하좌우에서 값이 1일때 방문 처리를 하고 0으로 만들준다.
2. 상하좌우가 0을 넘지않고, rows, cols를 넘어가지 않는지 확인한다.
3. 
### py code
```py
# 스택을 이용한 DFS풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != '1':
                    continue

                cnt += 1
                stack = [(row, col)]

                while stack:
                    x, y = stack.pop()
                    grid[x][y] = '0'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                            continue
                        stack.append((nx, ny))
        return cnt

```
### py code 02
```py
# recursive(재귀)로 DFS 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        def dfs_recursive(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return

            # 방문처리
            grid[r][c] = '0'
            for i in range(4):
                dfs_recursive(r + dx[i], c + dy[i])
            return

        for r in range(m):
            for c in range(n):
                node = grid[r][c]
                if node != '1':
                    continue

                cnt += 1
                dfs_recursive(r, c)

        return cnt

```