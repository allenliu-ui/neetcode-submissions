import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    result = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)
    while heap:
        resultPair = heapq.heappop(heap)
        num = resultPair[1]
        result.append(num)
    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
