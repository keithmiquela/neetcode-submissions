class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        currGas = 0
        for i in range(len(gas)):
            currGas += gas[i]
            if currGas < cost[i]:
                start = i+1
                currGas = 0
            else:
                currGas -= cost[i]
        for i in range(len(gas)):
            currGas += gas[i]
            if currGas < cost[i]:
                return -1
            else:
                currGas-=cost[i]
        if start >= len(gas):
            return -1
        return start