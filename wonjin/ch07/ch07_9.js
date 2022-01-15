let nums = [-1, 0, 1, 2, -1, -4];

var threeSum = function (nums) {
  const answer = [];
  nums.sort((a, b) => a - b);

  if (nums.length < 3) return answer; // 길이 2이하

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) return answer;
    if (nums[i] === nums[i - 1]) continue; //  경우의 수가 같음

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];
      if (sum === 0) {
        answer.push([nums[i], nums[left], nums[right]]);
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;
        left++;
        right--;
        continue;
      }

      if (sum > 0) {
        while (left < right && nums[right] === nums[right - 1]) right--;
        right--;
      } else {
        while (left < right && nums[left] === nums[left + 1]) left++;
        left++;
      }
    }
  }
  return answer;
};

console.log(threeSum(nums));
