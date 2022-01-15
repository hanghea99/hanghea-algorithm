/*
배열 파티션

n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

*/

const nums = [1, 4, 3, 2];

const solution = (nums) => {
  let sum = 0;
  pair = [];
  nums.sort((a, b) => a - b);
  // console.log(nums);
  for (i in nums) {
    pair.push(nums[i]);
    if (pair.length == 2) {
      // ES6 문법 사용 스프레드 문법
      sum += Math.min(...pair);
      // 그전
      // sum += Math.min.apply(Math, pair);
      pair = [];
    }
  }
  return sum;
};

console.log(solution(nums));
