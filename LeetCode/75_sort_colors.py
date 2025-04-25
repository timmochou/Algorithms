# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

def sortColors(nums):
    left_curr = 0
    curr = 0
    right_curr = len(nums) - 1
    # while curr place < right_curr, then
    while curr < right_curr:
        if nums[curr] == 0:
            #when nums curr = 0
            nums[left_curr], nums[curr] = nums[curr], nums[left_curr]
            left_curr += 1
            curr += 1
        elif nums[curr] == 2:
            nums[right_curr], nums[curr] = nums[curr], nums[right_curr]
            right_curr -= 1
        else:
            curr += 1
    return nums

print(sortColors([2,0,2,1,1,0]))



