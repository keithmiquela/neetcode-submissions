class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while heap:
            if len(heap) <= 1:
                break;
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x == y:
                continue;
            
            remainder = abs(x-y)
            heapq.heappush(heap, -remainder)
        
        if heap:
            return -heapq.heappop(heap)
        return 0