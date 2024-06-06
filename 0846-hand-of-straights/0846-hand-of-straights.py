class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        countes = Counter(hand)
        heap = sorted(countes.items())
        heapify(heap)
        
        while heap:

            temp = []
            cur, freq = heappop(heap)
            if freq - 1 > 0:
                temp.append((cur, freq - 1))
            
            for i in range(groupSize - 1):
                if not heap: return False
                nxt, nxt_freq = heappop(heap)
                if nxt - 1 != cur:
                    return False
                
                cur = nxt
                if nxt_freq - 1 > 0:
                    temp.append((nxt, nxt_freq - 1))
             
            while temp:
                heappush(heap, temp.pop())
        
        return True
                
                