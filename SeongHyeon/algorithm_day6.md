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

## 프로그래머스 [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586)

```py
from collections import deque
from math import ceil

def solution(progresses, speeds):
    days = deque([ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)])
    answer = []
    while days:
        complete = days.popleft()
        count = 1
        while days and days[0] <= complete:
            days.popleft()
            count += 1
        answer.append(count)
    return answer
```

## 프로그래머스 [다리를 지나는 트럭](https://programmers.co.kr/learn/courses/30/lessons/42583)

1차 풀이(시뮬레이션)

```py
from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = []
    input_idx, output_idx = 0, 0
    answer = 0
    while input_idx < len(truck_weights):
        if weight >= truck_weights[input_idx]: # 트럭이 들어갈 수 있을 때
            queue = [x - 1 for x in queue]
            queue.append(bridge_length)
            weight -= truck_weights[input_idx]
            answer += 1
            input_idx += 1
        else: # 트럭이 더이상 못 들어갈 때
            out =  queue.pop(0)
            queue = [x - out for x in queue]
            weight += truck_weights[output_idx]
            answer += out - 1
            output_idx += 1
    if queue:
        answer += queue[-1]

    return answer
```

2차 풀이(차의 남은 거리만 append)

```py
from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 들어가는/나가는 차의 index
    i, o = 0, 0
    queue = deque()
    answer = 0

    # 차가 전부 들어올 때까지
    while i < len(truck_weights):

        # 나갈 수 있는 차가 있을 때
        if queue and queue[0] == 0:
                queue.popleft()
                weight += truck_weights[o]
                o += 1

        # 차가 들어올 수 있을 때
        if weight >= truck_weights[i]:
            queue = deque([x - 1 for x in queue])
            queue.append(bridge_length - 1)
            weight -= truck_weights[i]
            i += 1
            answer += 1

        # 더이상 차가 들어올 수 없을 때
        else:
            answer += queue[0]
            queue = deque([x - queue[0] for x in queue])

    # 마지막 차가 나갈 때까지의 시간
    answer += queue[-1] + 1

    return answer
```
