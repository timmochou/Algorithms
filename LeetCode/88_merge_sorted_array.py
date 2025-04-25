def merge(nums):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    left_num = 0 
    curr_num = 1
    right_num = len(nums)-1

    # # definition of nums 2
    # left_num2 = 0
    # curr_num2 = 0
    # right_num2 = len(nums2)

    while curr_num <= right_num:
        # if curr_num <= left num
        if nums[curr_num] <= nums[left_num]:
            nums[curr_num], nums[left_num] = nums[left_num], nums[curr_num]
            curr_num +=1
            left_num +=1
        # if curr_num <= left num
        # elif nums[curr_num] > nums[right_num]:
        #     nums[curr_num],nums[right_num] = nums[right_num],nums[curr_num]
        #     curr_num -=1
        elif nums[curr_num] >= nums[right_num]:
            nums[curr_num], nums[right_num] = nums[right_num], nums[curr_num]
            right_num -=1
            curr_num -=1
        else:
            curr_num +=1
            left_num +=1

        
    
    return nums
    

print(merge([1,4,10,5,9,6,7]))