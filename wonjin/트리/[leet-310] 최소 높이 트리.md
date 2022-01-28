# [leet-310] 최소 높이 트리 [python]

## [문제](https://leetcode.com/problems/minimum-height-trees/) 

## 의사코드
- 이문제에서 그래프는 무방향이므로, 트리의 부모와 자식은 양쪽 노드 모두 graph 딕셔너리에 양방향 삽입하여 구성한다.
1. n은 전체 노드의 개수이므로 여기서 leaves, 즉 리프 노드의 개수만큼 계속 빼나가면서 최종 2개 이하가 남을 때까지 반복한다.
2. 마지막 남은 값이 홀수 개일 때는 루트가 최종 1개가 되지만 짝수 개일 떄는 2개가 될 수 있다. 따라서 while문은 2개까지는 계속 반복한다.
3. 무방향 그래프라 graph 딕셔너리에서 pop()으로 제거하고 연결된 값도 찾아서 제거한다.
### py code
```py
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=1:
            return [0]

        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # 첫 번째 리프 노드 추가
        leaves=[]
        for i in range(n):
            if len(graph[i])==1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 반복 제거
        while n>2:
            n -=len(leaves)
            new_leave=[]
            for leaf in leaves:
                # 연결된값 제거
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor])==1:
                    new_leave.append(neighbor)

            leaves = new_leave

        return leaves
```
