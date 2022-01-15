/* 
그룹 애너그램
같은 문자로 이루어져 있는 단어들을 찾아서 그룹화

조건
1. 동일한 문자로 이루어져 있어야됨
2. 동일한 문자로 이루어진 단어를 배열화
*/

const strs = ['eat', 'tea', 'ate', 'nat', 'bat'];
// [ [ 'eat', 'tea', 'ate' ], [ 'nat' ], [ 'bat' ] ]

const solution = (strs) => {
  let answer = [];
  let hash = {};

  strs.map((str) => {
    const word = str.split('').sort().join();
    // console.log(word);
    // console.log(hash);

    hash[word] ? hash[word].push(str) : (hash[word] = [str]);
  });
  /* Object.keys() 메소드는 주어진 객체의 속성 이름들을 일반적인 반복문과 동일한 순서로 순회되는 열거할 수 있는 배열로 반환*/
  let keys = Object.keys(hash);
  // console.log(keys);

  keys.map((key) => {
    // console.log(hash[key]);
    answer.push(hash[key]);
  });

  return answer;
};
// O(n^2)?

console.log(solution(strs));
