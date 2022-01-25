# BOJ 11725. 트리의 부모 찾기
#### https://www.acmicpc.net/problem/11725


```python
node_count = int(input())
# 0번째 노드는 무조건 공란, 1부터 node_count번째 노드들만 채워진다
tree = [] * (node_count + 1)
parents = [0] * (node_count + 1)

for _ in range(node_count-1):
    node0, node1 = map(int, input().split())
    tree[node0].append(node1)
    tree[node1].append(node0)
    
def dfs(root, tree, parents):
    for node in tree[root]:
        if parents[node] == 0:
            parents[node] = root
            dfs(node, tree, parents)
            
dfs(1, tree, parents)

for index in range(2, node_count+1):
    print(parents[index])
```
