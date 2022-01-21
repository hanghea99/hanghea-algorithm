# 바이러스
# https://www.acmicpc.net/problem/2606

computers_count = int(input())
pairs_count = int(input())
nodes = []
pairs = []

for i in range(pairs_count):
    com0, com1 = map(int, input().split())
    nodes.append(com0)
    nodes.append(com1)
    pairs.append([com0, com1])

keys = list(set(nodes))
graph = {key: [] for key in keys}

for pair in pairs:
    graph[pair[0]].append(pair[1])
    graph[pair[1]].append(pair[0])

result = []

def dfs(node):
    result.append(node)

    for adj in graph[node]:
        if adj not in result:
            dfs(adj)

dfs(1)
print(len(result) - 1)
