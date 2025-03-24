class Solution:
    def canPlaceFlowers(self, flowerbed, n: int) -> bool:
        zeroes = []
        x = 1
        for i in flowerbed:
            if i == 0:
                x += 1
            else :
                if x != 0:
                    zeroes.append(x)
                x = 0
        if x != 0:
            zeroes.append(x+1)

        y = sum(((i-1) // 2) for i in zeroes)
        print(zeroes)
        print(y)

        return y >= n

s = Solution()
print(s.canPlaceFlowers([1,0,0,0,1], 1))