class Solution:
    def findMin(self, nums: List[int]) -> int:
        temp = sorted(nums)
        return temp[0]