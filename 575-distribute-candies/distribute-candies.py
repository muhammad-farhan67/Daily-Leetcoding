class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        unique=set(candyType)
        half=n//2
        result=min(half,len(unique))
        return result