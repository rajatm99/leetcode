from collections import defaultdict
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        d = defaultdict(int)
        window = 1

        d[str1] += 1
        while window < len(str1):
            x = str1[:window] * (len(str1) // window)
            if x == str1 :
                d[str1[:window]] += 1        
            window += 1
        
        window = 1

        d[str2] += 1
        while window < len(str2):
            x = str2[:window] * (len(str2) // window)
            if x == str2 :
                d[str2[:window]] += 1        
            window += 1


        longest = 0
        result = ""
        for x,y in d.items():
            if y == 2 and len(x) > longest:
                longest = len(x)
                result = x
        return result


s = Solution()
print(s.gcdOfStrings("ababab", "abab"))
print(s.gcdOfStrings("leet", "code"))