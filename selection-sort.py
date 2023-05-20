    def select(self, arr, i):
        min = i
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j
        return min
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            j = self.select(arr,i)
            arr[i],arr[j] = arr[j],arr[i]
