class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        answer = [0] * len(nums)
        
        def merge(left, right):
            
            smallerCount = 0
            mergedArray = []
            
            leftPointer = 0
            rightPointer = 0
            
            while leftPointer < len(left) and rightPointer < len(right):
                if nums[right[rightPointer]] < nums[left[leftPointer]]:
                    mergedArray.append(right[rightPointer])
                    rightPointer += 1
                    smallerCount += 1
                
                else:
                    mergedArray.append(left[leftPointer])
                    answer[left[leftPointer]] += smallerCount
                    leftPointer += 1
            
            mergedArray.extend(right[rightPointer:])
            
            while leftPointer < len(left):
                mergedArray.append(left[leftPointer])
                answer[left[leftPointer]] += smallerCount
                leftPointer += 1
            
            return mergedArray

            

            
            
        def mergeSort(start, end):
            
            if start == end:
                return [start]
            
            mid = start + (end - start) // 2
            
            left = mergeSort(start, mid)
            right = mergeSort(mid + 1, end)
            
            return merge(left, right)
        
        

        mergeSort(0, len(nums) - 1)
        return answer
        