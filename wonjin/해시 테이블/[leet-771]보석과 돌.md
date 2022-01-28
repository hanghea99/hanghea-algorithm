# 보석과 돌 [python]

## [문제](https://leetcode.com/problems/jewels-and-stones/) 

## 의사코드
1. stones의 각 문자를 해시 테이블로 freqs 딕셔너리에 추가하고 개수를 저장합니다.
2. freqs 딕셔너리에서 jewels의 문자를 키로 값을 가지고있는 그 값들의 합이 보석의 개수가 된다.

### py code
```py
# 해시 테이블을 이용한 풀이
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs ={}
        count = 0

        for char in stones:
            if char not in freqs:
                freqs[char] =1
            else:
                freqs[char] +=1

        for c in jewels:
            if c in freqs:
                count +=freqs[c]
        return count
```
### py code 02
```py
# defaultdict을 이용한 풀이
from collections import defaultdict

class Solution:
    def numJewelsInStones(self,jewels: str, stones: str) -> int:
        freqs =defaultdict(int)
        count = 0

        for char in stones:
            freqs[char]+=1

        for c in jewels:
            if c in freqs:
                count +=freqs[c]
        return count
```

### py code 03
```py
# Counters를 이용한 풀이
import collections

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freqs = collections.Counter(S)  # 돌(S) 빈도 수 계산
        count = 0

        # 비교 없이 보석(J) 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count
```