# [leet-297] 이진트리 직렬화 & 역직렬화 [python]

## [문제](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) 

## 의사코드
- 이진트리 데이터 구조는 논리적인 구조다. 이를 파일이나 디스크에 저장하기 위해서는 물리적인 형태로 바꿔줘야 한다. 이를 직렬화라고 한다. 반대는 역직렬화다.
1. 논리적 구조인 이진 트리를 직렬화로 하나의 문자열로 만든다. "#"은 데이터가 없음을 나타낸다.
2. 역직렬화 함수에서 str문자열을 다시 논리적 구조 이진트리로 만들어 root노드를 반환한다.

### py code
```py
class Codec:
    # 직렬화
    def serialize(self, root):
        queue = collections.deque([root])
        result=['#']

        # 트리 BFS 직렬화
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')
        return ' '.join(result)

    
    # 역직렬화

    def deserialize(self, data):
        if data == "# #":
            return None

        nodes = data.split(" ")

        root = TreeNode(int(nodes[1]))
        queue=collections.deque([root])
        index=2

        # 빠른 런너처럼 자식 노드 결과를 먼저 확인 후 큐 삽입
        while queue:
            node = queue.popleft()
            if nodes[index] is not '#':
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
            index+=1

            if nodes[index] is not "#":
                node.right = TreeNode(int(nodes[index]))
                queue.append(node.right)
            index += 1

        return root
```
