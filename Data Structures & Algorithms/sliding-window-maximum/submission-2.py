import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # sliding window
        # declare hashmap
        count = {}
        # declare heap
        heap = []
        heapq.heapify(heap)

        # init hashmap and heap with first k values
        for num in nums[0:k]:
            count[num] = count.get(num,0) + 1
            heapq.heappush(heap, num * -1)

        # declare pointers
        i = 0
        j = k-1

        # declare return array
        max_list = []

        # helper: find max
            # peek at heap
            # find if heap[0] exists in hashmap
            # if not, pop and loop
            # return existing max
        def findMax():
            temp_max = heap[0] * -1
            while count.get(temp_max, 0) == 0:
                heapq.heappop(heap)
                temp_max = heap[0] * -1
            return temp_max

        # algorithm loop
        while j < len(nums):
            # find current max
            curr_max = findMax()
            # append current max
            max_list.append(curr_max)

            # remove value at i from hashmap
            num_i = nums[i]
            count[num_i] = count.get(num_i, 0) - 1
            # iterate i
            i+=1
            
            # iterate j
            j+=1
            # if exists, add value at j to hashmap
            if j >= len(nums):
                break
            num_j = nums[j]
            count[num_j] = count.get(num_j, 0) + 1
            # push new value
            heapq.heappush(heap, num_j * -1)
        
        # return array
        return max_list