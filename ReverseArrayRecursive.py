
# Recursive Function taking array, start index, and end index
def reverseArray(arr, start, end):
    #checking if start index is smaller than or equals to end index
    if start >= end:
        return

    #swapping value
    arr[start], arr[end] = arr[end], arr[start]
    #calling recursive function with incrementing start index and decrementing end index
    reverseArray(arr, start+1, end-1)


arr = [1,2,3,4,5,6]
print(arr)
reverseArray(arr, 0, 5)

print("reversed array: \n", arr)

