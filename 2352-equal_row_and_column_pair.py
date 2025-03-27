from collections import defaultdict
class Solution:
    def equalPairs(self, grid) -> int:
        r = defaultdict(int)
        c = defaultdict(int)
        for i in grid:
           r[str(i)] += 1
        for i in range(len(grid)):
            x = []
            for j in range(len(grid)):
                x.append(grid[j][i])
            c[str(x)] += 1
        print(r, c)
        count = 0
        for i in grid:
            print(r[str(i)] * c[str(i)], r[str(i)] , c[str(i)] )
            count += r[str(i)] * c[str(i)] 
            r[str(i)] = 0
        print(count)
        return count

s = Solution()
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))