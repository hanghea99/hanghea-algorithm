import collections

# DFS
def numIslands_dfs(grid):
    def dfs(i, j):
        if i < 0 or i > len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(i, j)
                count += 1

    return count


# BFS
def numIslands_bfs(grid):
    dr = [0, 0, 1, -1]
    dc = [1, 1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    count = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            count += 1
            q = collections.deque([(row, col)])

            while q:
                r, c = q.popleft()
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != '1':
                        continue
                    grid[nr][nc] = '0'
                    q.append((nr, nc))

    return count

if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(numIslands_bfs(grid))
