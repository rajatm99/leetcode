class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for i in range(len(num1)):
            print(ord(num1[i]) - ord('0'))
            n1 = (n1 * 10) + (ord(num1[i]) - ord('0'))
            print(n1)
        
        n2 = 0
        for i in range(len(num2)):
            print(ord(num2[i]) - ord('0'))
            n2 = (n2 * 10) + (ord(num2[i]) - ord('0'))
            print(n2)

        return str(n1 * n2)



s = Solution()
print(s.multiply("123", "456"))