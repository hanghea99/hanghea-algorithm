/*
가장 긴 팰린드롬
팰린드롬 : 앞뒤를 뒤집어도 똑같은 문자열

조건
문자열이 주어질 때 부분문자열 중 가장 긴 팰린드롬을 찾기


*/

const str1 = 'babad'; //"bab" || "aba"
const str2 = 'cbbd'; // "bb"

// 팰린드롬인지 확인
const isPalindrome = (str) => {
  const half = parseInt(str.length / 2);
  for (let i = 0; i < half; i++) {
    if (str[i] !== str[str.length - 1 - i]) return 0;
  }
  return 1;
};

// isPalindrome(str1);

const solution = (str) => {
  const len = str.length;
  for (let i = len; i > 0; i--) {
    for (let j = 0; j <= len - i; j++) {
      // slice() 메서드는 어떤 배열의 begin부터 end까지(end 미포함)에 대한 얕은 복사본을 새로운 배열 객체로 반환 MDN
      const slice = str.slice(j, i + j);
      const isPalin = isPalindrome(slice);
      if (isPalin) {
        const answer = slice;
        return answer;
      }
    }
  }
};

console.log(solution(str1));
console.log(solution(str2));
