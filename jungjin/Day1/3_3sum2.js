// 출처 https://velog.io/@goonerholic/LeetCode-3Sum

const nums = [-1, 0, 1, 2, -1, -4];

var threeSum = function (nums) {
  nums.sort((a, b) => a - b); // sort nums array in ascending order
  const firstPositive = nums.findIndex((num) => num > 0); // find index of first positive number

  // if there is no positive number,
  // if nums array contains at least three zeros, then return [[0, 0, 0]],
  // or, there is no valid case
  if (firstPositive === -1) {
    if (nums.filter((num) => num === 0).length >= 3) {
      return [[0, 0, 0]];
    }
    return [];
  }

  const answer = [];

  // only iterate through the numbers less than or equal to zero
  for (let i = 0; i < firstPositive; i++) {
    // skip the number that is equal to the previous one
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    const num = nums[i];

    let left = i + 1;
    let right = nums.length - 1;

    // from both side of the rest elements, find the pair that makes zero.
    while (left < right) {
      const sum = num + nums[left] + nums[right];
      if (sum > 0) {
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        answer.push([num, nums[left], nums[right]]);
        left++;
        right--;
        while (nums[left] === nums[left - 1] && left < right) {
          left++;
        }
        while (nums[right] === nums[right + 1] && left < right) {
          right--;
        }
      }
    }
  }
  return answer;
};

console.log(threeSum(nums));
