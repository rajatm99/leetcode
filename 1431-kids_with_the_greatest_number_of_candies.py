class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        _max = max(candies)
        result = []
        for i in candies:
            result.append(i + extraCandies >= _max)
        return result
    
s = Solution()
print(s.kidsWithCandies([2,3,5,1,3], 3))