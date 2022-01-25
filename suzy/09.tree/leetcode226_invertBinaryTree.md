# Leetcode 226. Invert Binary Tree
#### https://leetcode.com/problems/invert-binary-tree/

1. DFS (pre-order)
```python
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        # 가장 최근에 stack에 들어간 노드부터 꺼낸다
        node = stack.pop()
        if node:
            # swap 후 stack에 넣어 다음 자식 노드들을 꺼낸다
            # 루트 노드부터 가장 마지막 리프 노드까지 차례차례 swap
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
        
    return root
```

2. DFS (post-order)
```python
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    stack = collections.deque([root])
    
    while stack:
        # 가장 최근에 stack에 들어간 노드부터 꺼낸다
        node = stack.pop()
        if node:
            # 리프 노드까지 순회하면서 stack에 넣는다
            # stack에 다 넣은 후 리프 노드들부터 차례차례 swap
            stack.append(node.left)
            stack.append(node.right)
            node.left, node.right = node.right, node.left
            
    return root
```

3. BFS
```python
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: TreeNode) -> TreeNode:
    # 먼저 넣은 노드부터 꺼내기 위해 queue 사용
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
            
    return root
```