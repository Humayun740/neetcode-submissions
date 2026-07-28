class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = {}, {}
        index = 0

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        for j in countS:
            if countS[j] != countT.get(j, 0):
                return False

        return True