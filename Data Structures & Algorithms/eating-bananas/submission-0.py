class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_number = max(piles)

        def isValid(mid):
            sum = 0 
            for pile in piles:
                sum+= math.ceil(pile/mid)
            return h >= sum
        
        def split(low, high):
            
            mid = math.floor((high-low)/2 + low)

            if not isValid(mid):
                return split(mid+1, high)
            else:
                if low == mid:
                    return mid
                else:
                    return split(low, mid)
            
        return split(1, max_number)