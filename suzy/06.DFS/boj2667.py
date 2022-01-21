# 단지 번호 붙이기
# https://www.acmicpc.net/problem/2667

map_length = int(input())
grid = []

for _ in range(map_length):
    row = [int(num) for num in list(input())]
    grid.append(row)


def dfs(x, y, num):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid) or grid[x][y] != 1:
        return
    grid[x][y] = num
    dfs(x + 1, y, num)
    dfs(x - 1, y, num)
    dfs(x, y + 1, num)
    dfs(x, y - 1, num)

town_num = 2
town_count = 0
villages_list = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 1:
            dfs(i, j, town_num)
            town_count += 1
            town_num += 1

print(town_count)

for i in range(len(grid)):
    villages_list += grid[i]

villages_count = sorted([villages_list.count(i) for i in range(2, 2 + town_count)])

for count in villages_count:
    print(count)