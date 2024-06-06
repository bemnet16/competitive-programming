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
                c2, f2 = heappop(heap)
                if c2 - 1 != cur:
                    return False
                
                cur = c2
                if f2 - 1 > 0:
                    temp.append((c2, f2 - 1))
             
            while temp:
                heappush(heap, temp.pop())
        
        return True
                
                