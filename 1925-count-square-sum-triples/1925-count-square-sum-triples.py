class Solution:
    def countTriples(self, n: int) -> int:
        
        square_triples = 0
        
        for a in range(1, (n + 1)):
            for b in range(1, (n + 1)):
                   
                temp = sqrt((a **2) + (b ** 2))
                if temp.is_integer() and temp <= n:
                    square_triples += 1

        
        return square_triples
        