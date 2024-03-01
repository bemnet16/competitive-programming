class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        basket = defaultdict(int)
        left = 0
        max_fruits = 0
        cur_fruits = 0
        
        for i in range(len(fruits)):
            
            while fruits[i] not in basket and len(basket) == 2:
                
                if basket[fruits[left]] == 1:
                    del basket[fruits[left]]
                else:  
                    basket[fruits[left]] -= 1
                    
                cur_fruits -= 1
                left += 1
            
            
            basket[fruits[i]] += 1
            cur_fruits += 1
            
            max_fruits = max(max_fruits, cur_fruits)
        
        
        
        return max_fruits
            
            
        