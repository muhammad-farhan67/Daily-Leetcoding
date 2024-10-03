class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        a = len(word1)
        b = len(word2)
        for i in range(min(a,b)):
            res.append(word1[i])
            res.append(word2[i])
        res.append(word1[b:])
        res.append(word2[a:])
        return "".join(res)