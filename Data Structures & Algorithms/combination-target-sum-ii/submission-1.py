class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)

        i = 0
        results = []
        while i < len(candidates):
            num = candidates[i]
            if num == target:
                results.append([num])
            if num < target:
                result = self.combinationSum2(candidates[i+1:len(candidates)], target-num)
                for array in result:
                    results.append([num]+array)
            while i < len(candidates) and candidates[i] == num:
                i+=1
        return results
