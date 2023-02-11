class Solution:
  def findTheWinner(self, n: int, k: int) -> int:

    fr = [False] * n
    count = n
    fp = 0  

    while count > 1:
      for _ in range(k):
        while fr[fp % n]:
          fp += 1
        fp += 1
      fr[(fp - 1) % n] = True
      count -= 1

    fp = 0
    while fr[fp]:
      fp += 1

    return fp + 1
