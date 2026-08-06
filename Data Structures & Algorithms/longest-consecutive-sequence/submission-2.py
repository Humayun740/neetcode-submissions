class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        checked = set(nums)
        maxCount = 0

        for num in checked:
            if (num - 1) not in checked:
                longCount = 1
                flag = True
                curr = num
                while flag:
                    if (curr + 1) in checked:
                        longCount += 1
                    else:
                        flag = False
                    curr = curr + 1
                if longCount > maxCount:
                    maxCount = longCount
        return maxCount

         