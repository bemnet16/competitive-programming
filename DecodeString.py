class Solution:
  def decodeString(self, s: str) -> str:

    li = [] 
    result = ''
    temp = 0

    for c in s:
      if c.isdigit():
        temp = temp * 10 + int(c)
      else:
        if c == '[':
          li.append((result, temp))
          result = ''
          temp = 0
        elif c == ']':
          prevStr, num = li.pop()
          result = prevStr + num * result
        else:
          result += c

    return result
