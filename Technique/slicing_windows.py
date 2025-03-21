def slicingWindow(arr, k): # k is the window size, arr is the list
    # to find the max sequence sum in the array
    # determine the arr size
    n = len(arr)
    # n must large than k
    if n < k:
        
        return "invalid number of k!"
    # create the first sum of the list
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # iterate the num popleft the first, and append the end
    for i in range(n-k):
        # deduct the first and add the next number
        window_sum = window_sum - arr[i] + arr[k+i]
        # to compare the window_sum and the number of max_sum
        max_sum = max(max_sum,window_sum)
    
    return max_sum

    


print(slicingWindow([1, 4, 2, 10, 2, 3, 1, 0, 20],9))


