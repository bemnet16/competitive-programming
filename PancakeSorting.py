class Solution:
  def pancakeSort(self, A: List[int]) -> List[int]:
    ans = []

    for i in range(len(A), 0, -1):
      index = A.index(i)
      A[:index + 1] = A[:index + 1][::-1]
      A[:i] = A[:i][::-1]
      ans.append(index + 1)
      ans.append(i)

    return ans
