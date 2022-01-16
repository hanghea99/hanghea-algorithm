/*
배열 파티션

n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라

배열 입력값은 항상 2n개 

*/

const solution = (nums) => {
  let answer = 0;
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    if (i % 2 === 0) answer += nums[i];
  }
  return answer;
};

console.log(solution(nums));
