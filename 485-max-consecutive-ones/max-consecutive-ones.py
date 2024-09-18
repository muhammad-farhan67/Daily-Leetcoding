class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
                maximum = max(maximum,count)
            else:
                count = 0
        return maximum