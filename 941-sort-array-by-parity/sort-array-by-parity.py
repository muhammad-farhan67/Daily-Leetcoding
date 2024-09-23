class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        for i in nums:
            if i%2==0:
              even.append(i)
            if i%2==1:
              odd.append(i)
        result=even+odd
        return result 