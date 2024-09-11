class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
      result=[]
      fresult=[]
      for i in range(len(nums)):
        if nums[i]==target:
            result.append(i)
      if result==[]:
        return [-1,-1]
      else:
        
        fresult.append(min(result))
        fresult.append(max(result))
        return fresult
        
        