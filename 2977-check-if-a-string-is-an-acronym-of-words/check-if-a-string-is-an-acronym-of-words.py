class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        times=0
        if len(words)==len(s):
            for i in range(len(words)):
              if words[i].startswith(s[i]):
                  times+=1
                  if times==len(words):
                    return True
              else:
                return False
                    
                
        else:
            return False