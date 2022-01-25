# [leet-104] Maximum Depth of Binary Tree [python]

## [문제](https://leetcode.com/problems/maximum-depth-of-binary-tree/) 

## 의사코드
1. 문제에서 input값으로 리스트가 모두 들어오는 것으로 착각할 수 있다. root에는 최상위 루트 노드만 들어온다.
2. 예제 root = [3,9,20,null,null,15,7]에서 보면 3이 먼저 q에 들어가게된다. 루트 노드 3의 자식노드를 확인하고 있으면 q에 추가한다.
3. q에서 노드하나를 제거해서 cur로 받고 cur에서도 자식노드가 있다면 q에 추가하면서 반복적으로 깊이를 측정한다.

### py code
```py
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque([root])
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return depth
```
