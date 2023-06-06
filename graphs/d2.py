import heapq
            # prob1, no1 = heapq.heappop(maxHeap)
            #         heapq.heappush(maxHeap, [prob1*prob2,no2])
minH = [3,5,1,8,7,0,2,18,11,4]

ans = heapq.heappop(minH)

print(ans)
print(minH)

heapq.heapify(minH)
print(minH)