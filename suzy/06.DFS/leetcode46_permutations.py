import itertools

# Using DFS
def permute(nums):
    result = []
    nums_length = len(nums)

    def dfs(nums, path):
        if len(path) == nums_length:
            result.append(path)
            return

        for i in range(len(nums)):
            next_nums = nums[:]
            next_nums.remove(nums[i])
            dfs(next_nums, path+[nums[i]])

    dfs(nums, [])
    return result


# Using itertools
def itertoolsPermute(nums):
    return list(itertools.permutations(nums))

if __name__ == "__main__":
    nums = [1,2,3]
    print(permute(nums))