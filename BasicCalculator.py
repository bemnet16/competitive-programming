class Solution:
    def calculate(self, s: str) -> int:
        num, li, op = 0, [], "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if op == "+":
                    li.append(num)
                elif op == "-":
                    li.append(-num)
                elif op == "*":
                    li.append(li.pop()*num)
                else:
                    li.append(int(li.pop()/num))
                num = 0
                op = s[i]
        return sum(li)
