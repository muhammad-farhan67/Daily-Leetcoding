class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        n = len(words)
        res = []
        for i in range(n):
            if x in words[i]:
                res.append(i)
        return res
