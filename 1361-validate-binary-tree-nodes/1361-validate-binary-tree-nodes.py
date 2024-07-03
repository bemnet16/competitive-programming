class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        par = defaultdict(int)
        child = defaultdict(set)
        
        for i in range(len(leftChild)):
            
            left = leftChild[i]
            right = rightChild[i]
            
            if left != -1:
                if (i in child[left] or left in child[i]) or left in par:
                    return False
                child[i].add(left)
                par[left] = i
            
            if right != -1:
                if (i in child[right] or right in child[i]) or right in par:
                    return False
                child[i].add(right)
                par[right] = i
                
            if len(child[i]) > 2:
                return False
            
    
        def find(chd):
            if chd in vis:
                return -1
            vis.add(chd)
            if chd not in par:
                return chd
            
            parent = find(par[chd])
            par[chd] = parent
            return parent
        
        
        vis = set()
        root = find(0)
        if root == -1:
            return False
        for i in range(n):
            vis = set()
            fi = find(i)
            if fi == -1 or fi != root:
                return False
        return True