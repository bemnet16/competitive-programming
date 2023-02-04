#User function Template for python3

class Solution: 
    def select(self, arr, i):
        lenArr = len(arr)
        selectionSort(arr,lenArr)
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            for j in range((i + 1),n):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
