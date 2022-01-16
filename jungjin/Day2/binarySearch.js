// 이진 탐색
// 데이터는 반드시 정렬 되어있어야 한다.
// 시간복잡도 O(log n) 선형시간

let arr = [];

for (let i = 1; i <= 100; i++) {
  arr.push(i);
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function (nums, target) {
  let startIndex = 0;
  let endIndex = nums.length - 1;

  if (startIndex > endIndex) return endIndex;

  while (startIndex <= endIndex) {
    let midIndex = Math.floor((startIndex + endIndex) / 2);

    let data = nums[midIndex];

    if (data === target) {
      return midIndex;
    } else if (data > target) {
      endIndex = midIndex - 1;
    } else {
      startIndex = midIndex + 1;
    }
  }
  return -1;
};
const target = 30;
console.log(binarySearch(target, arr));
