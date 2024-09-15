class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        r = n-1
        for i in range(n):
            mid = (l + r)//2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]