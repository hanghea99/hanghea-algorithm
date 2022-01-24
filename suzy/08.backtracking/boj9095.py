'''
BOJ 9095. 123 더하기
https://www.acmicpc.net/problem/9095
'''


#

def dfs(nums, path, total):
    for num in nums:
        if sum(path) > total:
            return

        if sum(path) == total:
            result.append(path)
            return

        dfs(nums, path + [num], total)


nums = [3, 2, 1]

test_count = int(input())
for _ in range(test_count):
    result = []
    dfs(nums, [], int(input()))
    print(len(result))