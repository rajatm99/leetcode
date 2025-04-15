from collections import defaultdict
class Solution:
    def subarraySum(self, nums, k) -> int:
        pre = []
        count = 0
        d = defaultdict(int)
        pre.append(nums[0])
        for i in range(1, len(nums)):
            pre.append(nums[i] + pre[i-1])
        print(pre)
        for i in pre:
            if d[i-k] > 0:
                count += d[i-k]
            if i == k:
                count += 1
            d[i] += 1
        print("final dict - ", d)
        return count

s = Solution()
# print("result - ",s.subarraySum([1,1,1], 2))
# print("result - ",s.subarraySum([-1,-1,1], 0))
print("result - ",s.subarraySum([1,2,3], 3))
        