class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        common = {}
        
        for idx, word in enumerate(list1):
            common[word] = [idx, float("inf")]
        
        for idx, word in enumerate(list2):
            if word in common:
                common[word][1] = idx
        
        answer = []
        _min = float("inf")
        
        for word, idxs in common.items():
            
            if sum(idxs) < _min:
                _min = sum(idxs)
                answer.clear()
                answer.append(word)
                
            elif sum(idxs) == _min:
                answer.append(word)
        
        return answer