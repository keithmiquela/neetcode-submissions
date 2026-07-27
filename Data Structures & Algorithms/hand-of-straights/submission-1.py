class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = {}
        for num in hand:
            count[num] = 1 if not count.get(num) else count[num]+1
        for i in range(0,1000):
            while count.get(i) and count.get(i) != 0:
                for j in range(0,groupSize):
                    if not count.get(i+j):
                        return False
                    count[i+j]=count.get(i+j)-1
            
        return True

        # 1
        # 2 2
        # 3 3
        # 4 4 
        # 5