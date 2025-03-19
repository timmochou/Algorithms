def twoSum(nums, target):
    hash_map = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in hash_map: #如果需要的數字已經在雜湊表中
            return [hash_map[complement], i] # 傳回兩個數字的索引
        
        hash_map[num] = i

print(twoSum([1,4,5,9,3],12))
