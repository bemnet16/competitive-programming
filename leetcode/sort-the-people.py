class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        name_height = [(name, heights[i]) for i,name in enumerate(names)]
        name_height.sort(key = lambda x:x[1], reverse = True)
        answer = [name for name,height in name_height]
        return answer
        