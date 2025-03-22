class Solution:
    def moveZeroes(self, nums) -> None:
        z = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                z +=1
            else:
                nums[i-z] = nums[i]
        i = len(nums) -1
        print(z)
        while z > 0:
            nums[i] = 0
            z -= 1
            i -= 1
        print(nums)

s = Solution()
s.moveZeroes([0,1,0,3,12])