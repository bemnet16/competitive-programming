class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:

    count = collections.Counter(tasks)
    m_freq = max(count.values())
    ta_oc = (m_freq - 1) * (n + 1)
    nfeq = sum(value == m_freq for value in count.values())
    return max(ta_oc + nfeq, len(tasks))
