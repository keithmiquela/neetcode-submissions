import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for pile in piles:
            max_val = max(max_val, pile)

        i = 1 
        j = max_val

        min_k = max_val

        def findTime(rate: int) -> int:
            hours = 0
            for pile in piles:
                curr_hours = math.ceil(pile/rate)
                hours += curr_hours
            return hours

        while i <= j:
            mid = (i+j)//2

            time = findTime(mid)

            if time <= h:
                min_k = min(min_k, mid)
                j = mid - 1
            else:
                i = mid + 1
        return min_k
            
            