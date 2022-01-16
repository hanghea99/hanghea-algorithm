from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for idx, n in enumerate(nums):
        complement = target - n
        print(nums[idx+1:])
        if complement in nums[idx+1:]:
            print(nums[idx+1:].index(complement))
            print([idx, nums[idx+1:].index(complement)+(idx+1)])

            return [idx, nums[idx+1:].index(complement)+(idx+1)]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    twoSum(nums, target)
