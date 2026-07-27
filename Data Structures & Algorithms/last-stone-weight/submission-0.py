class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if not x==y:
                heapq.heappush(heap,-abs(x-y))
        if not heap:
            return 0
        return -heap[0]
