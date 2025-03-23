from functools import reduce
class Solution:
    def findMaxAverage(self, nums, k) -> float:
        sum = reduce(lambda x,y : x+y, nums[:k])
        sumArr = []
        for i in range(k, len(nums)):
            sum = sum - nums[i-k] + nums[i]
            sumArr.append(sum)
        return max(sumArr) / k



s = Solution()
print(s.findMaxAverage([0,4,0,3,2], 1))