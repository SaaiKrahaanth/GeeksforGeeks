#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        
        l=len(arr)
        for i in range(l):
            min_index=i
            for j in range(i+1,l):
                if arr[min_index]>arr[j]:
                    self.swap(arr,min_index,j)
                   
        return arr
                
                
    def swap(self,arr,a,b):
        arr[a],arr[b]=arr[b],arr[a]
        
        #code here


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = [int(i) for i in input().split()]

        obj = Solution()
        obj.selectionSort(arr)

        IntArray().Print(arr)
        print("~")

# } Driver Code Ends