class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        print(nums)
        res = set()

        for i, val in enumerate(nums):
            start = i + 1
            end = len(nums) -1
            new_sum = -1 * val

            while start < end :
                s = nums[start] + nums[end]
                if s == new_sum:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif s < new_sum:
                    start += 1
                else:
                    end -= 1
        return list(res)
        

s = Solution()
print(s.threeSum([0,0,0,0]))