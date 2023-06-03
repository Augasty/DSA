arr = [1,9,2,5,3,0,7]

def selsort(array):
    for i in range(len(array)):
        smallestidx = i

        # for each element, find the smallest element to its left
        for j in range(i+1,len(array)):
            if array[j] < array[smallestidx]:
                smallestidx = j 
        # and replace it with the smallest element
        array[i],array[smallestidx] = array[smallestidx] , array[i]

    print(array)
selsort(arr)
