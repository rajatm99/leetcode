from functools import reduce
class Solution:
    def productExceptSelf(self, nums):
        prefixProd  = [0] * len(nums)
        prefixProd[0] = nums[0]
        for i in range(1, len(nums)):
            prefixProd[i] = prefixProd[i-1]*nums[i]
        print(prefixProd)

        l = len(nums) - 1
        suffixProd = [0] * len(nums)
        suffixProd[l] = nums[l]
        for i in range(l-1, -1, -1):
            suffixProd[i] = suffixProd[i+1] * nums[i]
        print(suffixProd)

        result = []
        result.append(suffixProd[1])
        for i in range(1,len(nums)-1):
                result.append(suffixProd[i+1] * prefixProd[i-1])

        result.append(prefixProd[len(nums)-2])
        return result
    
s = Solution()
print(s.productExceptSelf([1,2,3,4]))