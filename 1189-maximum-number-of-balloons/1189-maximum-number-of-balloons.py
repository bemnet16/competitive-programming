class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        balloon = {'b':1, 'a':1, 'l':2, 'o':2, 'n':1}
        counter = Counter(text)
        
        
        instances = float('inf')
        for char in balloon:
            
            if char not in counter:
                return 0
            
            instance = counter[char] // balloon[char]
            instances = min(instances, instance)
        
        return instances
            
            
        