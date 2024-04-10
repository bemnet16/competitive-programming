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
        
        importances = defaultdict(int)
        employee_graph = defaultdict(set)
        
        for i in range(len(employees)):
            importances[employees[i].id] = employees[i].importance
            employee_graph[employees[i].id] = set(employees[i].subordinates)
        
        
        
        total_importance = 0
        
        def dfs(employee_id):
            
            nonlocal total_importance
            
            total_importance += importances[employee_id]

            
            for subordinate_id in employee_graph[employee_id]:
                dfs(subordinate_id)
                    
        
        
        dfs(id)
        return total_importance
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    