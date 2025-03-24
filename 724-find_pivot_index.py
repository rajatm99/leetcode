class Solution:
    def pivotIndex(self, nums) -> int:
        pre = []
        pre.append(nums[0])
        for i in range(1, len(nums)):
            pre.append(pre[i-1] + nums[i])
        
        suf = [0]*len(nums)

        suf[-1]=(nums[-1])
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] + nums[i]
        print(pre, suf)

        for i in range(len(pre)):
            if pre[i] == suf[i]:
                return i
        return -1
        

s = Solution()
print(s.pivotIndex([2,1,-1]))