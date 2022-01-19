# Algorithm Day5

## 17. [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        result = []
        nums = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        def recur(data, idx):
            if idx == len(digits):
                result.append(data)
                return
            for letter in nums[digits[idx]]:
                recur(data + letter, idx + 1)
        recur('', 0)
        return result
```

## 46. [Permutations](https://leetcode.com/problems/permutations/)

```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def permutations(data):
            if len(data) == len(nums):
                result.append(data)
                return
            for num in nums:
                if num not in data:
                    permutations(data + [num])
        permutations([])
        return result
```

```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permutations(nums)
```

## 77. [Combinations](https://leetcode.com/problems/combinations/)

```py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = range(1, n + 1)
        result = []
        def combinations(data, arr):
            if len(data) == k or arr == '':
                result.append(data)
                return
            for idx, num in enumerate(arr):
                combinations(data + [num], arr[idx + 1:])
        combinations([], nums)
        return result
```

```py
class Solution:
    def combine(self, nums: List[int]) -> List[List[int]]:
        return Combinations(nums)
```

## 백준 [단지번호 붙이기(DFS)](https://www.acmicpc.net/problem/2667)

```py
apartment = []
n = int(input())
for _ in range(n):
    apartment.append(list(map(int, input())))
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
result = []

def dfs(x, y):
    global count
    if apartment[x][y] == 0:
        return
    apartment[x][y] = 0
    count += 1    
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx >= n or xx < 0 or yy >= n or yy < 0:
            continue
        dfs(xx, yy)

for x in range(n):
    for y in range(n):
        if apartment[x][y]:
            count = 0
            dfs(x, y)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)
```

## 백준 [바이러스](https://www.acmicpc.net/problem/2606)

```py
n = int(input())
graph = {}
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a not in graph:
        graph[a] = [b]
    else:
        graph[a] += [b]
    if b not in graph:
        graph[b] = [a]
    else:
        graph[b] += [a]

def dfs():
    visited = set()
    stack = [1]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack += graph[node]
    return len(visited) - 1

print(dfs())
```