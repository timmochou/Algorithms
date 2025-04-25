def search(nums, target):
    low = 0
    high = len(nums)

    if low <= high:
        #
        mid = (low + high)//2
        guess = nums[mid]

