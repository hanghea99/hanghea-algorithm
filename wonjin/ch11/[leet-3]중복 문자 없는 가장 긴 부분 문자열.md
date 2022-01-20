# 보석과 돌 [JavaScript, node.js]


### py code
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used={}
        max_length = start =0
        for idx, c in enumerate(s):
            if c in used and start <=used[c]:
                #이미 등장한 문자라면 start 갱신
                start = used[c]+1
            else:
                #최대길이 갱신
                max_length = max(max_length, idx - start +1)

            # 현재 문자의 위치 갱신
            used[c] = idx
        return max_length
```
