def isArraySorted(arr):
    if len(arr) == 1:
        return True
    return arr[0] <= arr[1] and isArraySorted(arr[1:])

arr = [1,5,7,9,11,23]
print(isArraySorted(arr))