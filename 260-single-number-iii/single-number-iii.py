class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result=[]
        times=0
        for i in range(len(nums)):
           if nums.count(nums[i])==1:
              result.append(nums[i])
              times+=1
              if times==2:
                break
        return result