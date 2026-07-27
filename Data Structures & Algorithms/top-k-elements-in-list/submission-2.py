class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if not count.get(num):
                count[num]=1
            else:
                count[num]+=1
        heap = []
        for key in count.keys():
            heap.append([-count.get(key),key])
        heapq.heapify(heap)
        results = []
        for i in range(k):
            results.append(heapq.heappop(heap)[1])
        
        return results