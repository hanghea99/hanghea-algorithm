예외처리 항상 먼저 생각

# 그룹 애너그램

```py
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for str in strs:
            dic[''.join(sorted(str))].append(''.join(str))
        return dic.values()
```

# 가장 긴 팰린드롬 부분 문자열

```py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left_idx, right_idx):
            nonlocal answer
            if (left_idx < 0 or right_idx > len(s) - 1) or s[left_idx] != s[right_idx]:
                if right_idx - left_idx - 1 > len(answer):
                    answer = s[left_idx + 1:right_idx]
            else:
                expand(left_idx - 1, right_idx + 1)
        answer = s[0]
        for i in range(len(s) - 1):
            expand(i, i)
            expand(i, i + 1)
        return answer
```

# 세 수의 합

예외처리: 중복 제거가 중요

```py
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        for idx in range(len(nums) - 2):
            if idx != 0 and nums[idx] == nums[idx - 1]:
                continue
            if nums[idx] > 0:
                break
            l_idx, r_idx = idx + 1, len(nums) - 1
            while l_idx < r_idx:
                temp_sum = nums[idx] + nums[l_idx] + nums[r_idx]
                if temp_sum == 0:
                    answer.append([nums[idx], nums[l_idx], nums[r_idx]])
                    l_idx += 1
                    while l_idx < r_idx and nums[l_idx] == nums[l_idx - 1]:
                        l_idx += 1
                    r_idx -= 1
                    while r_idx > l_idx and nums[r_idx] == nums[r_idx + 1]:
                        r_idx -= 1
                elif temp_sum < 0:
                    l_idx += 1
                else:
                    r_idx -= 1
        return answer 
```

# 배열 파티션

직접 케이스들을 실험해 본 후 정렬한 후에 순서대로 묶었을 때가 가장 큰 합이라는 것을 알게 됨

```py
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
```
