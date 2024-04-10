"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        employee_graph = defaultdict(tuple)
        
        for employee in employees:
            employee_graph[employee.id] = (employee.importance, set(employee.subordinates))
        
        
        
        total_importance = 0
        
        def dfs(employee_id):
            
            nonlocal total_importance
            
            total_importance += employee_graph[employee_id][0]

            
            for subordinate_id in employee_graph[employee_id][1]:
                dfs(subordinate_id)
                    
        
        
        dfs(id)
        return total_importance
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    