class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def findDistance(e):
            x = e[0]
            y=e[1]
            return (x**2 + y**2)**.5
        
        return sorted(points, key=findDistance)[0:k]