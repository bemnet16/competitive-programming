class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    tem_li = []
    ope = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b),
    }

    for t in tokens:
      if t in ope:
        b = tem_li.pop()
        a = tem_li.pop()
        tem_li.append(ope[t](a, b))
      else:
        tem_li.append(int(t))

    return tem_li[0]
