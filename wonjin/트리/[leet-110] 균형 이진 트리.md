# [leet-110] 균형 이진 트리 [python]

## [문제](https://leetcode.com/problems/balanced-binary-tree/) 

## 의사코드
- AVL트리는 대표적인 자가 균형 이진 탐색 트리이기도 하다.
- 효율적인 이진트리를 구성하기 위해서는 이진트리를 최대한 균형있게 맞추는게 좋습니다!
- 균형트리의 정의 : 양쪽 자식 노드의 레벨이 1을 초과하여 차이나지 않아야 합니다.
### py code
```py
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return 0
            
            # 재귀 호출로 리프노드까지 내려간다.
            # 맨 마지막 노드에 이르면 left=0, right=0을 리턴하도록 구성했다.
            left = dfs(root.left)
            right = dfs(root.right)
            
            # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1증가
             # \ 이 기호를 쓰면 긴 코드를 가독성있게 나눌 수 있습니다!
            if left ==-1 or \
                 right==-1 or \
                    abs(left-right)>1:
                return -1
            
            return max(left, right) +1
    
        return dfs(root)!=-1
```
