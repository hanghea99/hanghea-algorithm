/*
세수의 합
배열을 입력 받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력

*/

const nums = [-1, 0, 1, 2, -1, -4];

/*
[
  [-1, 0, 1],
  [-1, -1, 2]
]
*/
let answer = [];
const solution = (nums) => {
  // console.log(nums.sort());
  nums.sort((a, b) => a - b);

  const answer = [];

  const len = nums.length;

  for (let i = 0; i < len - 2; i++) {
    if (i > 0 && nums[i] == nums[i - 1]) continue;

    let left = i + 1;
    let right = len - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum > 0) {
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        answer.push([nums[i], nums[left], nums[right]]);
        left++;
        right--;
        while (left < right && nums[left] === nums[left - 1]) {
          left++;
        }
        while (left < right && nums[right] === nums[right + 1]) {
          right--;
        }
      }
    }
  }
  return answer;
};

console.log(solution(nums));
