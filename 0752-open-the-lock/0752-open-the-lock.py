from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def possibleLock(idx, strs):
            slot = int(strs[idx])
            st1 = (slot + 1) % 10
            st2 = (slot - 1) % 10
            return ((strs[:idx] + str(st1) + strs[idx + 1:]), (strs[:idx] + str(st2) + strs[idx + 1:]))
            
        
        deadends = set(deadends)
        level = []
        if not "0000" in deadends:
            level.append("0000")
        visited = set(["0000"])
        turns = -1
        
        
        while level:
            
            next_level = []
            turns += 1
            
            for lock in level:
                
                if lock == target:
                    return turns
            
                for slot_index in range(4):

                    posLock1, posLock2 = possibleLock(slot_index, lock)
                    
                    if not (posLock1 in visited or posLock1 in deadends):
                        visited.add(posLock1)
                        next_level.append(posLock1)

                    if not (posLock2 in visited or posLock2 in deadends):
                        visited.add(posLock2)
                        next_level.append(posLock2)
            
            level = next_level
        
        return -1
                
                
                
                
                
                
                
                
                
                
            
            
            