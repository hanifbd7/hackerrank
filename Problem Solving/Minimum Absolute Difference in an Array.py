def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    dif = [arr[i + 1] - arr[i] for i in range(0, len(arr) - 1)]
    
    return(min(dif))
