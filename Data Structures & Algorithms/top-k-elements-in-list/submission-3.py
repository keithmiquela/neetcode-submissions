class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num]=count[num]+1 if count.get(num) else 1
        
        heap = [[-count[key], key] for key in count.keys()]
        heapq.heapify(heap)
        result = []
        for i in range(k):
            result.append((heapq.heappop(heap)[1]))
        
        return result

