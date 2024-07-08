from sortedcontainers import SortedSet

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        lg = n
        cur = 0
        
        friends = SortedSet(range(1, n + 1))

        while lg > 1:
            
            rem =  (cur + k) % lg - 1
            friends.discard(friends[rem])
            
            cur = rem if rem != -1 else 0
            lg -= 1
        
        
        return friends[0]
            