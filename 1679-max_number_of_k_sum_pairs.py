from collections import defaultdict
class Solution:
    def maxOperations(self, nums, k) -> int:
        d = defaultdict(list)
        for i in range(len(nums)):
            d[nums[i]].append(i)

        operations = 0
        for i in nums:
            if len(d[i]) != 0 and len(d[k-i]) != 0:
                try :
                    operations += 1
                    x = d[i].pop()
                    d[k-i].pop()
                except :
                    operations -= 1
                    d[i].append(x)
                    print("some error, dont care")
        return operations
    
s = Solution()
print(s.maxOperations([1,2,3,4], 5))
            