# Combinations [python]

## [문제](https://leetcode.com/problems/combinations/) 

## 의사코드
1. n은 1~n까지 숫자를 의미하며, k는 k자릿수입니다.
2. dfs를 [], start 숫자 1과 자릿수k를 인자로 넘긴다.
3. dfs 함수의 종료조건은 k가 0이되면 만들어진 list인 조합 elements를 복사해서 results에 추가하고 함수를 종료시킨다.
4. 1~4까지 반복문을 실행하고 elements에 1~4중 하나를 추가하고 dfs를 재귀적으로 다시 호출한다. 호출할때 elements와 i+1, k-1를 인자로 넘긴다.
5. elements에 하나의 요소가 추가되었고, 우리가 만들어야하는 조합은 k자릿수이기 때문에 채워야하는 자릿수는 k-1이되기 때문이다.


### py code
```py
# DFS로 K개의 조합 생성
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start:int, k:int):
            if k==0:
                results.append(elements[:])
                return

            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1,k-1)
                elements.pop()

        dfs([],1,k)
        return results    

```
### py code 02
```py
# itertools의 combinations메서드를 이용한 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list,itertools.combinations(range(1, n+1),k)))

```