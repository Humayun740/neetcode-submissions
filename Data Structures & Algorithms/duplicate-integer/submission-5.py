class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupelist = set()

        for n in nums:
            if n in dupelist:
                return True
            else:
                dupelist.add(n)
        return False