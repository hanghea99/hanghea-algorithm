# Algorithm Day4

## 771. [Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

```py
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        answer = 0
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                answer += 1
        return answer
```

라이브러리 사용 풀이

```py
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        counter = Counter(stones)
        for jewel in jewels:
            result += counter[jewel]
        return result
```

## 3. [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        result = l = 0
        for idx, char in enumerate(s):
            if char in dic and l <= dic[char]:
                l = dic[char] + 1
            else:
                result = max(result, idx - l + 1)
            dic[char] = idx
        return result
```

## 347. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
```

## 백준 [수 찾기](https://www.acmicpc.net/problem/1920)

```py
n = int(input())
num_set = set(input().split())
m = int(input())
for num in input().split():
    if num in num_set:
        print('1')
    else:
        print('0')
```

## 백준 [비밀번호 찾기](https://teamsparta.notion.site/a2f05982ca4b4702999f2abf96a852a4)

```py
n, m = map(int, input().split())
dic = dict()
for _ in range(n):
    site, password = input().split()
    dic[site] = password
for _ in range(m):
    print(dic[input()])
```
