class Robot:

    def __init__(self, width: int, height: int):
        
        self.width = width
        self.height = height
        self. cur_pos = -1
        
        self.dir_pos = [((0, 0), "South")] + [((i, 0), "East") for i in range(1, width)] + [((width - 1, j), "North") for j in range(1, height)] + [((k, height - 1), "West") for k in range(width - 2, -1, -1)] + [((0, l), "South") for l in range(height - 2, 0, -1)]
        
    def step(self, num: int) -> None:
        self.cur_pos = 0 if self.cur_pos == -1 else self.cur_pos
        self.cur_pos = (self.cur_pos + num) % (len(self.dir_pos))

    def getPos(self) -> List[int]:
        
        return [0,0] if self.cur_pos == -1 else self.dir_pos[self.cur_pos][0]

    def getDir(self) -> str:
        
        return "East" if self.cur_pos == -1 else self.dir_pos[self.cur_pos][1]
        
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()