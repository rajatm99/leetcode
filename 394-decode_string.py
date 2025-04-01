class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        w = ""
        s = s[::-1]
        num = ""
        stack.append(s[0])
        for i in s[1:]:
            print(stack)
            if  i == "[":
                if num != "":
                    print("else",w * int(num))
                    stack.append(w * int(num))
                    num = ""
                    w = ""
                while True:
                    x = stack.pop()
                    if x == "]":
                        break
                    else :
                        w += x
            elif i.isnumeric():
                num = i + num
                print("numm", num)
            else:
                if num != "":
                    print("else",w * int(num))
                    stack.append(w * int(num))
                    num = ""
                    w = ""
                stack.append(i)
        if num != "":
            print("else",w * int(num))
            stack.append(w * int(num))

        print(stack)
        return ''.join(stack[::-1])

               
    
s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
# print(s.decodeString("100[leetcode]"))
