from collections import defaultdict
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        if len(typed) < len(name):
            return False
        
        n_pointer = 0
        t_pointer = 0
        
        while n_pointer < len(name) and t_pointer < len(typed):
            
            if name[n_pointer] == typed[t_pointer]:
                n_pointer += 1
                t_pointer += 1
            
            elif n_pointer > 0 and t_pointer > 0 and name[n_pointer - 1] == typed[t_pointer]:
                t_pointer += 1
            
            else:
                return False
        
        for i in range(t_pointer, len(typed)):
            if typed[i] != name[n_pointer - 1]:
                return False
        
        if n_pointer < len(name):
            return False
        
        return True