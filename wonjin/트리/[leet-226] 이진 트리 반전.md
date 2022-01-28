# [leet-226] 이진 트리 반전 [python]

## [문제](https://leetcode.com/problems/invert-binary-tree/) 

## 의사코드
1. queue에 루트 노드를 넣고 BFS 탐색을 하면서 같은 레벨에 있는 노드끼리 스왑을 시켜줍니다.
2. 현재 노드의 자식노드가 있으면 queue에 추가한다. 없으면 None이 추가되고 이것은 if node: 조건에 걸린다. 
3. 모든 스왑이 완료되고 루트노드를 반환한다.
### py code
```py
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = collections.deque([root])
        
        # 부모 노드부터 하향식 스왑
        while queue:
            node = queue.popleft()
            
            if node:
                node.left, node.right = node.right, node.left
                
                queue.append(node.left)
                queue.append(node.right)
        
        return root
```

### py code02

```py
# 재귀적으로 이용한 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

         def invert(parent):
            if parent:
                parent.left, parent.right = invert(parent.right), invert(parent.left)
                return parent
        
         return  invert(root)
```