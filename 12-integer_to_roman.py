class Solution:
    def intToRoman(self, num: int) -> str:
        _map = {
            1:"I",
            5:"V",
            10:"X",
            50:"L",
            100:"C",
            500:"D",
            1000:"M",
        }
        result = ""
        place = 1
        while num > 0:
            temp = []
            d = num % 10
            if d <= 3:
                temp = [1] * d
            elif d == 4:
                temp = [1, 5]
            elif d <= 8:
                temp = [5] + ([1] * (d-5))
            elif d == 9:
                temp = [1, 10]
            temp = [place * i for i in temp]
            print(temp)
            r = ""
            for i in temp:
                r += _map[i]
            result = r + result
            print(result)
            place *= 10
            num = num // 10
                

        return result
    
s = Solution()
print(s.intToRoman(58))

        