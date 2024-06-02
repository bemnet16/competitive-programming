class Solution:
    def partitionString(self, s: str) -> int:
        
        cur = set()
        count = 1
        
        for char in s:
            if char in cur:
                count += 1
                cur = {char}
            else:
                cur.add(char)
        
        return count