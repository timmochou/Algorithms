def findsmallest(arr):
    # initialize the smallest number
    smallest = arr[0]
    # initialize the smallest number index
    smallest_index = 0
    # find the smallest number in the list
    for i in range(1, len(arr)):
        # if the number smaller than the smallest number then
        if arr[i] < smallest:
            # let the smallest number to this number
            smallest = arr[i]
            # index to this number
            smallest_index = i
    # return the smallest number index
    return smallest_index

def selection_sort(arr):
    #create a new list to store the number 
    newArr = []

    for i in range(len(arr)):
        smallest_index = findsmallest(arr)
        # pop(index) is the method to delete the number in the list
        # this action will append the smallest and delete that number in the original list
        newArr.append(arr.pop(smallest_index))
    return newArr

print(selection_sort([1,5,2,6,4,20]))
