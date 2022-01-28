# Permutations [python]

## [문제](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

## 의사코드
1. 서로 다른 숫자가 담긴 리스트를 넘겨받아서 모든 순열을 리턴해야한다.
2. dfs함수에 elements에 리스트가 인자로 전달된다. elements가 길이가 0일때 종료조건이 된다.
3. next_ele에는 dfs에 넘겨줄 인자값이 저장된다. [1,2,3] -> [2,3] -> [3]->[] -> 종료
4. prev_ele는 숫자가 하나씩 추가되면서 순열이 만들어진다. next_ele요소가 없을때 prev_ele에는 입력 nums의 길이만큼 요소를 가지게된다.



### py code
```py
# DFS를 활용한 순열 생성
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        prev_ele =[]

        def dfs(elements):
            if(len(prev_ele)==len(nums)):
                result.append(prev_ele[:])

            for i in elements:
                next_ele = elements[:]
                next_ele.remove(i)

                prev_ele.append(i)
                dfs(next_ele)
                prev_ele.pop()

        dfs(nums)
        return result
```
### py code 02
```py
# itertools의 permutations메서드를 이용한 풀이
# permutations메서드는 반환값을 튜플모음으로 반환하기 때문에  map으로 list로 만들어 줬다.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(map(list,itertools.permutations(nums)))
```