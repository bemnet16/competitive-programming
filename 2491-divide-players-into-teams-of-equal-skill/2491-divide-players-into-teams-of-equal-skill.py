class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        skill.sort()
        
        left = 0
        right = len(skill) - 1
        
        pre_sum = skill[0] + skill[-1]
        sum_chemistry = 0
        
        while left < right:
            
            cur_sum = skill[left] + skill[right]
            
            if cur_sum != pre_sum:
                return -1
            
            cur_product = skill[left] * skill[right]
            
            sum_chemistry += cur_product
            
            left += 1
            right -= 1
        
        
        
        return sum_chemistry