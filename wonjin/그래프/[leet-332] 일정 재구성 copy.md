# [leet-332] 일정 재구성 [python]

## [문제](https://leetcode.com/problems/reconstruct-itinerary/) 

## 의사코드
1. 일정을 딕셔너리에 키와 값으로 저장합니다. 중복된 일정인 경우 어휘 순으로 방문하기 때문에 sorted메서드로 정렬을 합니다.
2. route에 방문한 항공을 추가합니다. dfs 탐색을 하기때문에 마지막 항공이 리스트에 먼저 추가된다.
3. 탐색이 모두 종료되었을때 route에는 여행일정이 역순으로 저장되있다. 슬라이싱[::-1]으로 리스트를 역순으로 반환한다.
### py code
```py
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for a,b in sorted(tickets):
            graph[a].append(b)
        
        route=[]
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)

        dfs('JFK')
        return route[::-1]
```