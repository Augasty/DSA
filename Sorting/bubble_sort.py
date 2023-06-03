def bubble(arr):
    swapped = False

    for idx in range(len(arr)):

        for j in range(len(arr) - idx - 1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j],arr[j+1]=arr[j+1], arr[j]
        if not swapped:
            return




arr = [1,9,2,5,3,0,7]
bubble(arr)
print(arr)