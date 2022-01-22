# Algorithm Day7

## 78. [Subsets](https://leetcode.com/problems/subsets/)

```py
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(data, idx):
            if idx >= len(nums):
                result.append(data)
                return
            dfs(data, idx + 1)
            dfs(data + [nums[idx]], idx + 1)
        dfs([], 0)
        return result
```

## 332. [Reconstruct Itinerary](https://leetcode.com/problems/reconstruct-itinerary/)

```py
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        answer = []
        ck = True
        for ticket in sorted(tickets):
            graph[ticket[0]].append(ticket[1])

        def dfs(data, now):
            nonlocal answer, ck
            if not graph[now]:
                if len(data) == len(tickets) + 1:
                    answer = data
                    ck = False
                    return
                else:
                    return
            for idx, node in enumerate(graph[now]):
                graph[now].pop(idx)
                dfs(data + [node], node)
                if ck == False:
                    break
                graph[now].insert(idx, node)

        dfs(['JFK'], 'JFK')
        return answer
```

## 207. [Course Schedule](https://leetcode.com/problems/course-schedule/)

```py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 생성
        graph = defaultdict(list)
        # 배울 수 있는 코스들 초기화(선행 과정이 없는 아이들만 남기기)
        learned = set([x for x in range(numCourses)])
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            if prerequisite[0] in learned:
                learned.remove(prerequisite[0])

        while True:
            # 한 루프 끝날동안 삭제가 발생했는지 확인
            ck = True
            # 빈 딕셔너리 저장 공간
            delete_nums = []
            for key, values in graph.items():
                for idx, value in enumerate(values):
                    # 배운 과정일 경우 graph에서 삭제
                    if value in learned:
                        del values[idx]
                        ck = False
                if not values:
                    # 빈 배열을 가진 키 learned에 저장하고 graph에서 삭제
                    learned.add(key)
                    delete_nums.append(key)
            for delete_num in delete_nums:
                del graph[delete_num]
            # 삭제가 발생하지 않았다면 루프 종료
            if ck == True:
                break
        # 배울 수 있는 숫자가 numCourses와 동일한지 반환
        return len(learned) == numCourses
```
