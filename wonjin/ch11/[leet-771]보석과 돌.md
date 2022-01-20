# 보석과 돌 [JavaScript, node.js]

## [문제](https://leetcode.com/problems/jewels-and-stones/) 

## 의사코드

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