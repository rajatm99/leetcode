class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        print(x)
        y = ""
        while x :
            y += x.pop() + " "
        print(y)
        return y[:-1]

s = Solution()
print("|"+s.reverseWords(" hello world ")+"|")