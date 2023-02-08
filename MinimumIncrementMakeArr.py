class Solution:
  def minIncrementForUnique(self, A: List[int]) -> int:

    result = 0
    m_av = 0
    A.sort()

    for a in A:
      result += max(m_av - a, 0)
      m_av = max(m_av, a) + 1

    return result
