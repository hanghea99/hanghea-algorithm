import collections

# DFS
def findItinerary_dfs(tickets):
    graph = collections.defaultdict(list)
    for dep, arr in sorted(tickets):
        graph[dep].append(arr)

    result = []

    def dfs(dep):
        while graph[dep]:
            dfs(graph[dep].pop(0))
        result.append(dep)

    dfs('JFK')
    return result[::-1]

# BFS
def findItinerary_bfs(tickets):
    graph = collections.defaultdict(list)
    for dep, arr in sorted(tickets):
        graph[dep].append(arr)

    result = []
    queue = collections.deque(['JFK'])

    while queue:
        node = queue.popleft()
        result.append(node)

        if graph[node]:
            next_node = graph[node].pop(0)
            queue.append(next_node)

    return result

if __name__ == "__main__":
    tickets = [
        ["JFK", "SFO"],
        ["JFK", "ATL"],
        ["SFO", "ATL"],
        ["ATL", "JFK"],
        ["ATL", "SFO"]
    ]
    print(findItinerary_bfs(tickets))

    tickets = [
        ["MUC", "LHR"],
        ["JFK", "MUC"],
        ["SFO", "SJC"],
        ["LHR", "SFO"]
    ]
    print(findItinerary_bfs(tickets))