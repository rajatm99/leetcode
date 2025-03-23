class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        v = sum(1 for char in s[:k] if char in vowels)
        print(v)
        countArr = []
        countArr.append(v)
        for i in range(k, len(s)):
            if s[i] in vowels:
                v += 1
            if s[i-k] in vowels:
                v -= 1
            countArr.append(v)
        return max(countArr)


s = Solution()
print(s.maxVowels("leetcode", 3))