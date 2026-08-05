class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num
        res = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                tempProduct = 1
                for j in range(len(nums)):
                    if j == i:
                        continue
                    tempProduct *= nums[j]
                res[i] = tempProduct 
            else:
                res[i] = int(product / nums[i])

        return res