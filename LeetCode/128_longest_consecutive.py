def longestConsecutive(nums):
    
    sort = sorted(nums)
    curr = 0
    left = 1
    right = len(nums)-1
    result = 0
    while curr < right:
        #check whether the number is the same
        if sort[curr] == sort[left]:
            left +=1
            curr +=1
        elif sort[curr] + 1 == sort[left]:
            result += 1
            left += 1
            curr +=1
        else:
            curr +=1

    if len(sort) == 1:
        return 1
    elif len(sort) == 0:
        return 0
    elif result > 0:
        return result + 1
    else:
        result

    
    
print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

