def findmax(list):
    # if len(list)==2, compare that two number
    if len(list)==2:
        return list[0] if list[0]>list[1] else list[1]
    else:
        sub_max = findmax(list[1:])
        return list[0] if list[0]> sub_max else sub_max

print(findmax([1,5,10,2]))