# 중복 문자 없는 가장 긴 부분 문자열 [python]
## [문제](https://leetcode.com/problems/jewels-and-stones/)
### 의사코드
1. 딕셔너리에는 문자인 키와 인덱스 값으로 이루어져있다.
2. enumerate로 문자열의 문자와 인덱스를 가져온다. 해당 문자가 이미 등장한 문자이면서 시작위치가 이미등장한 문자의 인덱스보다 작거나 같다면 start를 한 칸 옆으로 움직인다.
3. 아니라면 최대 길이를 갱신다. 이전 max_length와 현재의 최대길이 중 max값으로 갱신한다.
4. 이미 등장한 문자가 다시 나왔다면 딕셔너리에 이전 인덱스값을 현재 인덱스값으로 갱신한다.
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
