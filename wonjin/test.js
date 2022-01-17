let nums = [6, 2, 6, 5, 1, 2];

var arrayPairSum = function (nums) {
  nums.sort((a, b) => a - b);
  const answer = nums.filter((_, i) => i % 2 === 0);
  return answer.reduce((sum, cur) => sum + cur, 0);
};

console.log(arrayPairSum(nums));
