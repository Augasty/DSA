def insertion_sort(arr):

     # For each item in the input list
    for idx in range(len(arr)):

        # Shift it to the left until it's in the right spot
        while idx>0 and arr[idx]>arr[idx-1]:
            arr[idx],arr[idx-1] = arr[idx-1],arr[idx]
            idx -= 1


arr = [1,9,2,5,3,0,7]
insertion_sort(arr)
print(arr)