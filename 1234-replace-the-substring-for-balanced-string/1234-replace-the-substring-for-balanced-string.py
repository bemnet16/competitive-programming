class Solution:
    def balancedString(self, s: str) -> int:
        
        char_occurence = {"Q":0, "W": 0, "E": 0, "R":0}
        balanced_num = len(s) // 4
        
        
        
        def checkBalance(temp_occurence):
            
            return all(char_occurence[char] - temp_occurence[char] <= balanced_num for char in char_occurence)
        
        
        
        
        for char in s:
            char_occurence[char] += 1
        
        min_length = len(s)
        left = 0
        temp_occurence = defaultdict(int)
        
        if checkBalance(temp_occurence):
            return 0
        
        for right, char in enumerate(s):
            
            temp_occurence[char] += 1
            
            while checkBalance(temp_occurence):
                
                min_length = min(min_length, (right - left + 1))
                temp_occurence[s[left]] -= 1
                left += 1
        
        
        return min_length
            
            