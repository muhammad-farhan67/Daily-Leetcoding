class Solution:
    def minLength(self, s: str) -> int:
        stk = []
        for i in range(len(s)):
           if not stk:
                  stk.append(s[i])
           elif stk[-1]=="A" and s[i]=="B" or stk[-1]=="C" and s[i]=="D":
                  stk.pop()
           
           else:
                  stk.append(s[i])

        return len(stk)

             
