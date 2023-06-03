def combine_sorted(list1, list2):
    idx1 = 0
    idx2 = 0

    merged = []

    while idx1 < len(list1) and idx2 < len(list2):
        if list1[idx1] <= list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1

    while idx1 < len(list1):
        merged.append(list1[idx1])
        idx1 += 1
    while idx2 < len(list2):
        merged.append(list2[idx2])
        idx2 += 1
    
    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return combine_sorted(left,right)


arr = [1,9,2,5,3,0,7]
arr = merge_sort(arr)
print(arr)
# damn
# O(nlogn) time
#O(n) space