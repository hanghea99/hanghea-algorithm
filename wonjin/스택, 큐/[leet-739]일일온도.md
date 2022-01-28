# [leet-739] 일일온도 [Python]

## [문제]() 
## 의사 코드
- 배열로 들어온 온도의 인덱스의 차이를 이용한다.
1. answer에 T길이 만큼 0으로 초기화된 배열을 생성한다.
2. T의 요소를 순회하면서 index와 cur 요소값으로 반복한다.
3. 스택에 요소가 있고 && cur이 T[스택 마지막 요소의 idx]보다 크면 스택의 요소 pop한다.
4. last에는 제거된 요소의 index가 저장된다. 현재 cur의 인덱스 i에서 제거된 요소의 인덱스 last를 뺀 값이 기다려야하는 날짜가 된다.
5. 스택에 요소가 없고, 이전보다 온도가 낮다면 스택에 인덱스 i를 추가합니다.


#### py code
```py
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer =[0]* len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last]= i-last
                
            stack.append(i)
            print(stack)
        return answer
  
```