class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        addition = 0
        arr=[]
        for i in nums:
         addition += i
         arr.append(addition)
        return arr