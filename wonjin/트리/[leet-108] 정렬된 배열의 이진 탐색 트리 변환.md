# [leet-108] 정렬된 배열의 이진 탐색 트리 변환 [python]

## [문제](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/) 

## 의사코드
- BST는 이진 검색의 마법을 적용한 이진 트리다.
- 따라서 BST를 만들기 위서는 정렬된 배열을 이진 검색으로 계속 쪼개 나가기만 하면 된다.
### py code
```py
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums)//2
        
        node= TreeNode(nums[mid])
        node.left = sortedArrayToBST(nums[:mid])
        node.right = sortedArrayToBST(nums[mid+1:])        
        
        return node
```
