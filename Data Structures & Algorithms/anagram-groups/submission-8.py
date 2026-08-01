class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outputs = []
        visited = set()
        for i in range(len(strs)):
            if i in visited:
                continue
            answers = []
            currWord = "".join(sorted(strs[i]))
            answers.append(strs[i])
            visited.add(i)
            for j in range(i+1, len(strs)):
                if j in visited:
                    continue
                nextWord = "".join(sorted(strs[j]))
                if nextWord == currWord:
                    answers.append(strs[j])
                    visited.add(j)
            outputs.append(answers)
        return outputs