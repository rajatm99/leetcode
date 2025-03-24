class Solution:
    def largestAltitude(self, gain) -> int:
        pre = []
        pre.append(0)
        for i in range(len(gain)):
            pre.append(pre[i] + gain[i])
        print(pre)
        return max(pre)

s = Solution()
print(s.largestAltitude([52,-91,72]))