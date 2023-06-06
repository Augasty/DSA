# de shaw round 1 question

def degreeof(arr):
    map = {}
    for idx in range(len(arr)):
        if arr[idx] not in map:
            map[arr[idx]] = [0,idx,idx]
        
        map[arr[idx]][0] += 1
        map[arr[idx]][2] = idx

    degree = 0
    for ele in map:
        if map[ele][0] >= degree:
            degree = map[ele][0]

    start = 0
    end = float('inf')
    
    for ele in map:
        if map[ele][0] == degree and map[ele][2] - map[ele][1] < end - start:
            end = map[ele][2]
            start = map[ele][1]

    return [degree,start,end+1]

array = [1,2,1,1,2,4,5,2,1,7]
result = degreeof(array)
print(result[0])
print(array[result[1]:result[2]])

