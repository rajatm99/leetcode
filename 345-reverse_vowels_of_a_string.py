class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vIndex = []
        for i in range(len(s)) :
            if s[i] in vowels:
                vIndex.append(i)


        x= ""
        for i in range(len(s)) :
            if s[i] in vowels:
                x += s[vIndex.pop()]
            else :
                x += s[i]
           

        return x

s = Solution()
print(s.reverseVowels("IceCreAm"))
