def maxSubArray(nums):
    total = 0
    result = nums[0]
    # iterate the num in the list
    for i in nums:
        # if total less than 0, total reset to 0
        if total < 0:
            total = 0
        # if not less than 0, total + the next i
        total += i
        # compare the total and result, find the max within total and result
        result = max(total, result)


    return result

print(maxSubArray([5,4,-1,7,8]))