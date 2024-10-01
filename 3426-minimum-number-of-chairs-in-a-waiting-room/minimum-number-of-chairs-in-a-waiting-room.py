class Solution:
    def minimumChairs(self, s: str) -> int:
        count=0
        countmax=0
        for i in range(len(s)):
            if s[i]=='E':
                count+=1
                countmax=max(countmax,count)
            if s[i]=='L':
                count-=1
        return countmax