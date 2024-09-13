class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
         n = len(numbers)
         i=0
         lo,hi=i,n-1
         while lo < hi:
            if numbers[lo]+numbers[hi] > target:
                hi -=1
            elif numbers[lo]+numbers[hi] < target:
                lo+=1 
            elif numbers[lo]+numbers[hi] == target:
                return [lo+1,hi+1]