class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heap = nums
        heapq.heapify(heap)
        while len(heap)>k:
            heapq.heappop(heap)
        self.heap, self.k = heap, k

    def add(self, val: int) -> int:
        heap = self.heap
        k = self.k
        heapq.heappush(heap, val)
        if len(heap) > k:
            heapq.heappop(heap)
        return heap[0]
