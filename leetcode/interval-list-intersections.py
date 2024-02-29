from collections import OrderedDict

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        answer = OrderedDict()
        
        f_pointer = 0
        s_pointer = 0
        
        while f_pointer < len(firstList) and s_pointer < len(secondList):
            
            f_start, f_end = firstList[f_pointer]
            s_start, s_end = secondList[s_pointer]
            
            if s_start <= f_start and f_end <= s_end:
                answer[(f_start, f_end)] = (f_start, f_end)
            
            elif f_start <= s_start and s_end <= f_end:
                answer[(s_start, s_end)] = (s_start, s_end)
            
            elif s_start <= f_start and f_start <= s_end:
                answer[(f_start, s_end)] = (f_start, s_end)
            
            elif f_start <= s_start and s_start <= f_end:
                answer[(s_start, f_end)] = (s_start, f_end)
            
            
            if f_end < s_end:
                f_pointer += 1
            
            else:
                s_pointer += 1

                
                
        return answer.keys()
        