import itertools

# DFS
# [1, n], all possible combinations of k
def combine(n, k):
    result = []

    def dfs(nums, path):
        if len(path) == k:
            result.append(path)
            return

        for i in range(len(nums)):
            dfs(nums[i+1:], path+[nums[i]])

    dfs([num for num in range(1, n+1)], [])
    return result


# Using itertools
def itertoolsCombine(n, k):
    return list(itertools.combinations(range(1, n+1), k))

if __name__ == "__main__":
    print(combine(4,2))