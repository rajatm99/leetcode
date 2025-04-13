class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals,key = lambda x : x[0])
        x = intervals[0]
        i = 1
        y = None
        new = []
        while i < len(intervals):
            y = intervals[i]    
            if x[1] >= y[0]:
                x[1] = max(x[1], y[1])
            else :
                new.append(x)
                x = y
            y = None
            i += 1
        new.append(x)
        if y :
            new.append(y)
        return new

        

s = Solution()
print(s.merge([[1,4],[4,5]]))
print(s.merge([[2,6], [1,3],[8,10],[15,18]]))