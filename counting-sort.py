def countingSort(arr):
    count = [0] * (max(arr)+1)  
    sorted_arr = [0] * len(arr)
    
    for i in arr:       #an array to count each time a value appears
        count[i] +=1
        
    for i in range(1,len(count)):      #find the cumulative sum of the counts
        count[i] += count[i-1]
        
    for i in reversed(arr):
        sorted_arr[count[i]-1] = i
        count[i] -= 1

    return sorted_arr
