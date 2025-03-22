class Solution:
    def compress(self, chars) -> int:
        if len(chars) == 0:
            return 0
        
        c = chars[0]
        f = 0
        result = []
        for i in chars:
            if i == c :
                f += 1
            else:
                result.append(c)
                if f != 1:
                    x= []
                    while f > 0 :
                        x.append(str(f%10))
                        f = f // 10
                    x.reverse()
                    result+=x
                c = i
                f = 1
        result.append(c)
        if f != 1:
            x = []
            while f > 0 :
                x.append(str(f%10))
                f = f // 10
                print(x)
            x.reverse()
            print(x)
            result += x
        chars[:] = result
        print(chars)
        return len(result)
    
s = Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

