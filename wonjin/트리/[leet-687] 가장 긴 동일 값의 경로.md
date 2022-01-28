# [leet-687] 가장 긴 동일 값의 경로 [python]

## [문제](https://leetcode.com/problems/longest-univalue-path/) 

## 의사코드
- 이진 트리의 직경 문제와 유사하다. 
1. 루트 노드에서부터 DFS로 재귀 탐색을 진행하면서 리프에 도달하도록 한다.
2. 리프에 도달하면 그때부터 현재 노드 값과 자식노드값이 같은지 백트래킹하면서 거리를 누적해 나간다.

### py code
```py
class Solution:
    result:int =0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            # 존재하지 않는 자식노드 리턴값             
            if not node:
                return 0

            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left= dfs(node.left)
            right= dfs(node.right)

            # 현재 노드가 자식 노드와 동일한 경우 거리 1증가
            if node.left and node.left.val == node.val: 
                left+=1
            else:
                left=0
            if node.right and node.right.val == node.val :
                right+=1
            else: 
                right=0
            
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최댓값이 결과가 된다.
            self.result = max(self.result , left+right)

            # 상태값
            return max(left, right)

        dfs(root)
        return self.result
```
