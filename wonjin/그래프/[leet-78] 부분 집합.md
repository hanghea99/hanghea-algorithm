# [leet-78] 부분 집합 [python]

## [문제](https://leetcode.com/problems/number-of-islands/) 

## 의사코드
1. 경로 path를 만들어 나가면서 인덱스를 1씩 증가하는 형태로 깊이 탐색한다. 
2. 별도의 종료 조건 없이 탐색이 끝나면 저절로 함수가 종료되게 한다. 
3. 모든 탐색의 경로가 결국 정답이 되므로 탐색할 때마다 매번 결과를 추가하면된다.


### py code
```py
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result=[]

        def dfs(index, path):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path +[nums[i]])

        dfs(0,[])
        return result

```
