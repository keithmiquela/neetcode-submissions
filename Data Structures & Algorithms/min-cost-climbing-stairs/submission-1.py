class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total_steps = len(cost)
        A = [0]*(total_steps+1)
        A[total_steps-1] = cost[total_steps-1]
        for i in range(total_steps-2,-1,-1):
            A[i] = min(A[i+1],A[i+2])+cost[i]

        return min(A[0],A[1])