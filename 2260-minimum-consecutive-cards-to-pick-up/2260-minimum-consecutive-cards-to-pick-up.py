class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        
        seen_cards = {}
        min_cons = len(cards) + 1
        
        for i in range(len(cards)):
            
            if cards[i] in seen_cards:
                min_cons = min(min_cons, (i - seen_cards[cards[i]] + 1))
                del seen_cards[cards[i]]
            
            seen_cards[cards[i]] = i
        
        
        
        return min_cons if min_cons < len(cards) + 1 else -1