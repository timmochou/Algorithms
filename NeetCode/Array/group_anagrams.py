def groupAnagrams(strs):
    hash_map = {}
    # iterate the string in the list
    for s in strs:
        # sort the string
        sort = tuple(sorted(list(s)))
        # if this string not in hash_map
        if sort in hash_map:
            hash_map[sort].append(s)
        else:
            hash_map[sort] = [s]
    return hash_map.values()

print(groupAnagrams(["act","pots","tah","hat"]))
