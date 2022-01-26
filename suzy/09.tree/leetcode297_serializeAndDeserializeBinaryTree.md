# Leetcode 297. Serialize and Deserialize Binary Tree
#### https://leetcode.com/problems/serialize-and-deserialize-binary-tree/


1. Serialization
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root: TreeNode) -> str:
    # return을 None으로 처리할 경우, 문자열 변환 안 됨
    # 또한 -1000 < root.val < 1000 조건이 있으므로, -1 등의 int값으로 처리하면 안 됨
    if not root:
        return '*'
    
    return '.'.join([str(root.val), serialize(root.left), serialize(root.right)])
```

2. Deserialization
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deserialize(data: str) -> TreeNode:
    if data[0] == '*':
        return None
    
    # 재귀를 위해서는 data가 str 타입을 유지해야하므로
    # split() 통해 리스트로 만들지 않고, "," 기준으로 slicing
    node = TreeNode(data[:data.find(',')])
    node.left = deserialize(data[data.find(',')+1:])
    node.right = deserialize(data[data.find(',')+1:])

    return node
```
