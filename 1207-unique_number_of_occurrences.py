from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        d = defaultdict(int)
        for i in arr :
            d[i] += 1
        s = set(d.values())
        return len(d.values()) == len(s)