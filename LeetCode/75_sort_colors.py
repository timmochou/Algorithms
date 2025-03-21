def sortColors(nums):
    """ red = 0, white = 1, blue = 2
    don't use sort funciton"""
    left = 0
    curr = 0
    right = len(nums) - 1

    # when current index <= right
    while curr <= right:
        if nums[curr]==0:
            # if current value = 0 , switch with left
            nums[left], nums[curr] = nums[curr], nums[left]
            # because left = 0, so left need to add 1 and curr need to add 1
            left += 1
            curr +=1
        elif nums[curr]==2:
            # if current value = 2, switch with left
            nums[right], nums[curr] = nums[curr], nums[right]
            # now the right number is two, so right -=1 to check
            right -= 1
        else:
            curr += 1
    return nums

    # return list
print(sortColors([2,0,2,1,1,0]))

    
