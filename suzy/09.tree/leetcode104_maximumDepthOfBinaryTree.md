# Leetcode 104. Maximum Depth of Binary Tree
#### https://leetcode.com/problems/maximum-depth-of-binary-tree/

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root:TreeNode) -> int:
    if root is None:
        return 0
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            # 해당 depth의 특정 노드의 자식 노드들을 queue에 넣는다
            if cur_node.left:
                queue.append(cur_node.left)
            if cur_node.right:
                queue.append(cur_node.right)
    
    return depth
```