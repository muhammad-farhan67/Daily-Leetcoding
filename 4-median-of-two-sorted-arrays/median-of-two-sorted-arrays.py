class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        if len(merged)%2==1:
            median = float(merged[len(merged)//2])
            return median
        else: 
            med1 = float(merged[len(merged)//2])
            med2 = float(merged[len(merged)//2-1])
            median = (med1+med2)/2.0
            return median