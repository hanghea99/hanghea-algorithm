import collections

# DFS
def subsets_dfs(nums):
    result = []

    def dfs(nums, path):
        result.append(path)

        for i in range(len(nums)):
            dfs(nums[i + 1:], path + [nums[i]])

    dfs(nums, [])
    return result

# BFS
def subsets_bfs(nums):
    result = collections.deque()
    result.append([])

    for num in nums:
        for _ in range(len(result)):
            prev = result.popleft()

            next = list(prev)
            next.append(num)

            result.append(prev)
            result.append(next)

    return result

if __name__ == "__main__":
    nums = [1,2,3]
    print(subsets_bfs(nums))