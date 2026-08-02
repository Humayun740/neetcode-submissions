class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        final = []

        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i], 0) + 1
        
        mF = dict(sorted(m.items(), key=lambda item: item[1], reverse=True))

        results = list(mF.keys())

        for i in range(k):
            final.append(results[i])

        return final
        
        
        