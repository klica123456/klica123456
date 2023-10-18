from heapq import heappop, heappush
import sys

def push_num(num):
    if len(max_heap) == len(min_heap):
        heappush(max_heap, -num)
    else:
        heappush(min_heap, num)
    if min_heap and -max_heap[0] > min_heap[0]:
        temp_min = heappop(min_heap)
        temp_max = heappop(max_heap)
        heappush(max_heap, -temp_min)
        heappush(min_heap, -temp_max)
    print(-max_heap[0])


N = int(sys.stdin.readline())
max_heap = []
min_heap = []
for _ in range(N):
    push_num(int(sys.stdin.readline()))
