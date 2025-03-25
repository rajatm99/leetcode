class Solution:
    def findDifference(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2-s1)]
s = Solution()
print(s.findDifference([1,2,3], [2,4,6]))