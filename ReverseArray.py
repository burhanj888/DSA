
# Function to reverse array
def reverseArray(arr, start, end):
    #check start index is less than end index, when start index is bigger then end index it means value already swapped.
    while start < end:

        #swapping with start and end value until start index = end
        arr[start], arr[end] = arr[end], arr[start]

        # changing start and end index number, started with start= 0 and end= 4, then start=1 and end=3, then start=2 end=2
        start += 1
        end -= 1

arr = [1,2,3,4,5,6,7,8]
print(arr)

reverseArray(arr, 0, 7)
print("reverse array: \n", arr)