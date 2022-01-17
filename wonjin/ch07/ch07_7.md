#  두 수의 합[JavaScript, python] 

## 문제 설명
정수 배열과 정수가 주어지면 nums 두 숫자의 인덱스를target 반환 하여 합이 .target
각 입력에 정확히 하나의 솔루션 이 있다고 가정 하고 동일한 요소를 두 번 사용하지 않을 수 있습니다 .
어떤 순서로든 답변을 반환할 수 있습니다.

## 입력
- 입력: nums = [2,7,11,15], target = 9
- 출력: [0,1]
- 설명: nums[0] + nums[1] == 9이므로 [0, 1]을 반환합니다.
- 
## 제약:
- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- 유효한 대답은 하나만 존재합니다.

### 의사코드 

### Code
```js
```
```py
def twoSum(nums: List[int], target: int) -> List[int]:
    for idx, n in enumerate(nums):
        complement = target - n
        print(nums[idx+1:])
        if complement in nums[idx+1:]:
            print(nums[idx+1:].index(complement))
            print([idx, nums[idx+1:].index(complement)+(idx+1)])

            return [idx, nums[idx+1:].index(complement)+(idx+1)]
```
