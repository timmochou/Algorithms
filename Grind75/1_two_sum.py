def twosum(list ,target):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]+list[j]== target:
                return [list[i],list[j]]
    return []


numbers = [1,2,5,4,15]
target = 20
print(twosum(numbers,target))