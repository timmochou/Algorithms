def isAnagram(s, t):
    s_list = list(s)
    t_list = list(t)     
    hash_map_s = {}
    hash_map_t = {}

    for i in s_list:
        if i  in hash_map_s:
            hash_map_s[i] += 1
            
        else:
            hash_map_s[i] = 1
    for j in t_list:
        if j  in hash_map_t:
            hash_map_t[j] += 1 
            
        else:
            hash_map_t[j] = 1
            
    
    if hash_map_s == hash_map_t:
        return True
    return False
