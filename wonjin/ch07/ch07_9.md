# 세 수의 합[JavaScript] 

## 문제 설명
정수 배열 nums을 감안할 때, 모든 세 쌍둥이를 반환 [nums[i], nums[j], nums[k]]하는 등 i != j, i != k,와 j != k,와 nums[i] + nums[j] + nums[k] == 0.

솔루션 세트에는 중복 트리플렛이 포함되어서는 안 됩니다.
## 입출력
- 입력: 숫자 = [-1,0,1,2,-1,-4]
- 출력: [[-1,-1,2],[-1,0,1]]
## 제약
- 0 <= nums.length <= 3000
- -105 <= nums[i] <= 105
### 의사코드 

### Code
```js
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

```