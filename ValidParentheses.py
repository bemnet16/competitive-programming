class Solution:
  def isValid(self, s: str) -> bool:
    tem_li = []

    for char in s:
      if char == '(':
        tem_li.append(')')
      elif char == '{':
        tem_li.append('}')
      elif char == '[':
        tem_li.append(']')
      elif not tem_li or tem_li.pop() != char:
        return False

    return not tem_li
