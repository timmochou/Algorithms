def minSubArrayLen(nums, target):
    # initial the curr_sum and left(started index) to 0
    left = curr_sum = 0
    # initial the min_length to float
    min_length = float('inf')

    # initial the result to None
    result = None

    # iterate the num of the list
    for right in range(len(nums)):
        # add the right edge to the curr_sum
        curr_sum += nums[right]

        # if the curr_sum larger than target, dequeue the left num
        while curr_sum >= target:
            if right - left +1 < min_length:
                min_length = right - left + 1
                result = right - left + 1
            curr_sum -= nums[left]
            left += 1
    return result if result else 0            



print(minSubArrayLen([2,3,1,1,1,1,1,1],7))