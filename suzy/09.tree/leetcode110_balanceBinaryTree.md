# Leetcode 297. Serialize and Deserialize Binary Tree
#### https://leetcode.com/problems/balanced-binary-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root: Optional[TreeNode]) -> bool:
    def dfs(root):
        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        
        # 만약 왼쪽 자식 노드만 있고, 오른쪽 자식 노드는 없는 경우 -> left = 
        
        return max(left, right) + 1

    return dfs(root) != -1
```
