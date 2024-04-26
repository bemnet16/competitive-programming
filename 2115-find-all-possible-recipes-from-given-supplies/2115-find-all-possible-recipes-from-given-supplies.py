from collections import deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        outDegree = defaultdict(int)
        adjGraph = defaultdict(set)
        supplies = set(supplies)
        
        for recipe in range(len(recipes)):
            outDegree[recipes[recipe]] = 0
            for ingredient in ingredients[recipe]:
                if ingredient not in supplies:
                    adjGraph[ingredient].add(recipes[recipe])
                    outDegree[recipes[recipe]] += 1
        
        
            
        queue = deque()
        
        for recipe in recipes:
            if outDegree[recipe] == 0:
                queue.append(recipe)
                outDegree[recipe] -= 1
        
        
        answer = []
        
        while queue:
            
            for _ in range(len(queue)):
                
                recipe = queue.popleft()
                answer.append(recipe)
                
                for recipeIngrident in adjGraph[recipe]:
                    outDegree[recipeIngrident] -= 1
                    if outDegree[recipeIngrident] == 0:
                        queue.append(recipeIngrident)
                        
        
        
        return answer
                    
        
        
