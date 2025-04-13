class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            _sum = digits[i] + carry
            digits[i] = _sum % 10
            if _sum < 10:
                return digits
            carry = _sum // 10
        if carry != 0 :
            return [carry] + digits
        
s = Solution()
print(s.plusOne([9,9,9,9,9]))