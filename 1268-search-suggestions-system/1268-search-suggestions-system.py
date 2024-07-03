class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        heapify(products)
        answer = []
        
        for i in range(len(searchWord)):
            cur = searchWord[:i + 1]
            temp = []
            
            while products and not products[0].startswith(cur):
                heappop(products)
            
            j = 0
            while j < 3 and products and (products[0].startswith(cur)): 
                    temp.append(heappop(products))
                    j += 1
                    
            answer.append(temp)
            
            for c in temp:
                heappush(products, c)
        
        
        return answer
            
        
        
        
        
        
        