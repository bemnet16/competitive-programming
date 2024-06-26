class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pos_speed = sorted(zip(position, speed), reverse=True)
        stack = []
        
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if stack and time > stack[-1]:
                stack.append(time)
            
            if not stack:
                stack.append(time)
        
        return len(stack)
                
                