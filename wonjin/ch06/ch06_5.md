# 그룹 애너그램 [JavaScript] 

## 문제 설명
문자열 배열이 주어지면 아나그램을 함께 그룹화하십시오. 어떤 순서로든 답변을 반환할 수 있습니다.

Anagram은 일반적으로 모든 원래 문자를 정확히 한 번 사용하여 다른 단어 또는 구의 문자를 재배열하여 형성된 단어 또는 구입니다.

## 입력
Input: strs = ["eat","tea","tan","ate","nat","bat"]

## 출력
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

## 제약:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] 영문 소문자로 구성되어 있습니다.

### 의사코드 

### Code
```js
function solution(arr) {
  let obj = {};

  for (let word of arr) {
    let s_sort = word.toLowerCase().split("").sort().join("");

    if (obj.hasOwnProperty(s_sort)) {
      obj[s_sort].push(word);
    } else {
      obj[s_sort] = [word];
    }
  }
  return Object.values(obj);
}
```
