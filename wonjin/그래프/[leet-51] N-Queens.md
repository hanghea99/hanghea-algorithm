# [leet-51] N-Queens [python]

## [문제](https://leetcode.com/problems/n-queens/) 

## 의사코드
row 는 퀸을 놓을 행번호를 의미한다.
dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
...
dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.


### py code
```py
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited = [-1] * n
        cnt = 0
        answers = []

        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.
        def is_ok_on(nth_row):
            for row in range(nth_row):
                if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                    return False
            return True

        def dfs(row):
            # dfs종료조건
            if row >= n:
                nonlocal cnt
                cnt += 1

                # 출력 형식 만듬
                grid = [['.'] * n for _ in range(n)]
                for idx, value in enumerate(visited):
                    grid[idx][value] = 'Q'
                result = []
                for row in grid:
                    result.append(''.join(row))
                answers.append(result)
                return

            # visited[row] 의 값을 결정한다.
            # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)

        dfs(0)
        return answers
```
