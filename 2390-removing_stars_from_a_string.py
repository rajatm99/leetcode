class Solution:
    def removeStars(self, s: str) -> str:
        l = list(s)
        print(l)
        result = ""
        i = 0
        while len(l)> 0:
            x = l.pop()
            if x != "*":
                if i > 0:
                    i -= 1
                else :
                    result = x + result
            else :
                i += 1

        return result

s = Solution()
print(s.removeStars("leet**cod*e"))