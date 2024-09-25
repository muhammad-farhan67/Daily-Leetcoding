class Solution:
    def findLucky(self, arr: List[int]) -> int:
        unique=set(arr)
        times=0
        maxnum=0
        res=[]
        for i in unique:
            times=arr.count(i) 
            if times==i:
               res.append(i)
        if res==[]:   
          return -1
        return max(res)