class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexI = 0
        indexJ = 1
        numI = nums[indexI]
        numJ = nums[indexJ]

        while indexI < len(nums):
            while indexJ < len(nums):
                numI = nums[indexI]
                numJ = nums[indexJ]
                if numI+numJ == target:
                    print(indexI)
                    print(indexJ)
                    return [indexI, indexJ]
                else:
                    indexJ = indexJ + 1
            indexI = indexI + 1
            indexJ = indexI + 1
        
        
        