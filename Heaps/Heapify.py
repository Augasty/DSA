def heapify(heap, index):
    length = len(heap)
    while index < length:
        left_index  = index*2 + 1
        right_index = index*2 + 2

        if left_index >= length:
            break
        larger = left_index
        if right_index <= length and heap[larger] < heap[right_index]:
            larger = right_index

        if heap[index] < heap[larger]:
            heap[index], heap[larger] = heap[larger], heap[index]

            index = larger
        else:
            break
            # We're larger than both children, so we're done


# here i = 0, 0th element isn't following heap structure
array = [1,14,10,8,7,9,3,2,4,6]
heapify(array,0)
print(array)