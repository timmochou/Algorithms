def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

print(count([1,5,2,3,1,4]))