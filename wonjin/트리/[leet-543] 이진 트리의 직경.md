# [leet-543] 이진 트리의 직경 [python]

## [문제](https://leetcode.com/problems/diameter-of-binary-tree/) 

## 의사코드
- 상태값은 리프노드에서 현재 노드까지의 거리다.
- 거리는 왼쪽 자식 노드의 상태값과 오른쪽 자식 노드의 상태값의 함에 2를 더한 값이다.

1. 왼쪽, 오른쪽 리프 노드부터 시작해서 각노드의 상태값을 반환한다.
2. 루트 노트의 두 자식노드의 상태값에 2를 더한 값과 이전에 구한 longest값중 최대값이 가장 긴 경로의 길이가 된다.
3. 2를 더한 이유는 자식노드와 루트 노드의 길이를 의미한다.

### py code
```py
class Solution:
    longest: int =0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> int:
            # 존재하지 않는 자식노드 리턴값             
            if not node:
                return -1
            
            # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
            left= dfs(node.left)
            right= dfs(node.right)
            
            # 가장 긴 경로
            self.longest = max(self.longest, left + right + 2)

            # 상태값
            return max(left, right)+1
        
        dfs(root)
        return self.longest
```
