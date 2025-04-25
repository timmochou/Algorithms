def maxSlidingWindow(nums, k):
    # nums is the list
    # k is the size of sliding window
    # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    # Output: [3,3,5,5,6,7]
    max_array = []
    # compare the nums in the sliding window
    for i in range(len(nums)-k + 1):
        new_array = sorted(nums[i:i+k])
        max_array.append(new_array[k-1])
    return max_array
        
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
