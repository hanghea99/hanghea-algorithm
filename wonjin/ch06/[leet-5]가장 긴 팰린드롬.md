# 가장 긴 팰린드롬 부분 문자열 [JavaScript] 

## 문제 설명
문자열이 주어지면 에서 가장 긴 회문 부분 문자열 을 s반환 합니다 .s
## 입력
입력: s = "babad"

## 출력
 출력: "bab"
 설명: "aba"도 유효한 대답입니다.

## 제약:
- 1 <= s.length <= 1000
- s 숫자와 영문으로만 구성되어 있습니다.

### 의사코드 

### Code
```js
var longestPalindrome = function (s) {
  // 0~1 글자이거나 팰린드롬인 문자열 반환
  if (s.length < 2 || s === s.split("").reverse().join("")) {
    return s;
    }
    
  let result = ""; // 초기 세팅 (빈 문자열)
  for (let i = 0; i < s.length - 1; i++) {
    // 현재 최대 길이 팰린드롬 문자열과 현재 위치 i로 부터 짝수, 홀수 길이로 최대 팰린드롬 검사
    result = [result, expand(i, i + 1), expand(i, i + 2)].sort((a, b) => {
      return b.length - a.length; // 길이 기준 내림차순 sorting하여 가장 처음 값 반환
    })[0];
      
      
    console.log(
      [result, expand(i, i + 1), expand(i, i + 2)].sort((a, b) => {
        return b.length - a.length; // 길이 기준 내림차순 sorting하여 가장 처음 값 반환
      })
    );
  }
  return result;

  function expand(l, r) {
    //r==s.length까지 검사하는 이유는 substring에서 맨 끝 인덱스가 짤리기 때문이다
    while (l >= 0 && r <= s.length && s[l] == s[r - 1]) {
      l -= 1;
      r += 1;
      console.log("l :" + l, "r:" + r);
    }
    return s.substring(l + 1, r - 1);
  }
};
```

