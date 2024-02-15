class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        # track rabbits whose answer is the same 
        rabbits = {}
        
        for answer in answers:
            # /answer + 1/ to include the rabbits itself answerd in the array.
            rabbits[answer + 1] = rabbits.get((answer + 1), 0) + 1
        
        num_rabbits = 0

        for same_color in rabbits:

            temp = ceil(rabbits[same_color] / (same_color)) * (same_color)
            num_rabbits += temp
        
        return num_rabbits