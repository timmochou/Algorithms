def topKFrequent(nums, k):
    # create the hash map
    hash_map = {}
    # iterate the num in the nums and use get +1 to count the num
    for num in nums:
        hash_map[num] = hash_map.get(num,0) + 1
    # sort the num in the dict and reverse the value to the descending
    sort = dict(sorted(hash_map.items(), key = lambda x : (-x[1], x[0])))
    # select the top k number in the dict
    sort_k = dict(list(sort.items())[:k])
    # select the key in the list
    top_k_key = list(sort_k.keys())

    return top_k_key

print(topKFrequent([1,1,1,1,2,2,3,3,3],2))



