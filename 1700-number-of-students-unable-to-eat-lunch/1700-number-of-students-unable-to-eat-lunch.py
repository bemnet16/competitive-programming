from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        students = deque(students)
        sandwiches = deque(sandwiches)
        
        while students:
            
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            
            else:
                if len(set(students)) == 1:
                    return len(students)
                students.append(students.popleft())
                
        return 0   
        