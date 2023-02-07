class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    li_temp = []
    index = 0

    for x in pushed:
      li_temp.append(x)
      while li_temp and li_temp[-1] == popped[index]:
        li_temp.pop()
        index += 1

    return not li_temp
