class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       i = len(s)-1
       times=0
       while i>=0 and s[i]==' ':
            i-=1
       while i>=0 and s[i]!=' ':
            i-=1
            times+=1    
       return times 