class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        diffarr = []
        for n1, n2 in zip(nums1, nums2):
            diffarr.append(n1 - n2)
        
        answer = 0
        
        def merge(left, right):
            nonlocal answer
            
            mergedArray = []
            
            leftPointer = 0
            rightPointer = 0
            thirdPointer = 0
            
            
            while leftPointer < len(left) and rightPointer < len(right):
                if right[rightPointer] < left[leftPointer]:
                    
                    
                    while thirdPointer < len(left) and left[thirdPointer] <= right[rightPointer] + diff:
                        
                        thirdPointer += 1
                    
                    answer += thirdPointer
                    mergedArray.append(right[rightPointer])
                    rightPointer += 1
                
                else:
                    
                    mergedArray.append(left[leftPointer])
                    leftPointer += 1
            
            while rightPointer < len(right):
                while thirdPointer < len(left) and left[thirdPointer] <= right[rightPointer] + diff:
                        
                        thirdPointer += 1
                    
                answer += thirdPointer
                mergedArray.append(right[rightPointer])
                rightPointer += 1


            while leftPointer < len(left):
                mergedArray.append(left[leftPointer])
                leftPointer += 1
            
            return mergedArray
        
        
        def mergeSort(start, end):
            
            if start == end:
                return [diffarr[start]]
            
            mid = start + (end - start) // 2
            
            left = mergeSort(start, mid)
            right = mergeSort(mid + 1, end)
            
            return merge(left, right)
        
        
        mergeSort(0, len(diffarr) - 1)
        return answer
    
    