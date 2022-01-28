# Letter Combinations of a Phone Number [python]

## [문제](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) 

## 의사코드
1. 번호에 해당되는 알파벳을 딕셔너리로 만들어 저장한다.
2. 입력된 번호로 만들 수 있는 모든 숫자 조합을 리스트에 저장해서 반환한다.
3. 숫자마다 반복문이 실행되면 그안에서 문자마다 dfs를 호출한다. 호출할때 i는 시작 인덱스를 뜻하며 +1된 값을 넘겨준다. path에는 문자가 하나씩 추가된다
4. path의 길이와 digits의 길이가 같으면 result에 만들어진 문자조합 path를 추가하고 dfs가 종료된다.

### py code
```py
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return

        result=[]

        def dfs(index, path):
            if len(path)==len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                # print("i::" ,index)
                for j in dict[digits[i]]:
                    # print('dfs: (',i+1,path+j,")")
                    dfs(i+1, path+j)


        dict = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        dfs(0,'')


        return result
```
