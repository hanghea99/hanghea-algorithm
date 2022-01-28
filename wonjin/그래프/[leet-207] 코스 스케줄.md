# [leet-207] 코스 스케줄 [python]

## [문제](https://leetcode.com/problems/course-schedule/) 

## 의사코드
1. 딕셔너리에 코스 스케줄을 저장한다. 키값에 있는 코스를 완료하기 위해서는 value에 있는 값들을 끝내야한다.
2. 탐색중에 traced에 이미 있는 요소라면 순환 구조를 가졌다는 의미이다. False를 반환한다.

### py code
```py
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)
        # 그래프 구성

        for x,y in prerequisites:
            graph[x].append(y)

        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)


            # 탐색 종료 후 방문 노드 추가
            visited.add(i)
            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False
        return True

```