# Leetcode 543. Diameter of Binary Tree
#### https://leetcode.com/problems/diameter-of-binary-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: TreeNode):
    result = 0
    
    # return : 현재 노드에서 리프 노드까지의 거리
    def dfs(node: TreeNode) -> int:
        if not node:
            return -1
        
        # 자식 노드들 입장에서의 리프 노드까지의 거리
        left = dfs(node.left)
        right = dfs(node.right)

        # 현재 저장해놓은 결과값 vs.
        # 왼쪽 자식 노드 + 오른쪽 자식 노드 + 현재 노드에서 자식 노드들간 거리(2) 비교
        result = max(result, left + right + 2)
        
        # 자식 노드들 중에서 제일 긴 거리 + 현재 노드와 자식 노드 간의 거리(1)
        return max(left, right) + 1

    dfs(root)
    return result
```