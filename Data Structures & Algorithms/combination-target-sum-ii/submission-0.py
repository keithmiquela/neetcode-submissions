class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)[::-1]
        result = []
        def addNext(stack, total_sum, candidates):
            if not candidates:
                return
            candidate = candidates[0]
            if candidate + total_sum < target:
                temp = stack.copy()
                temp.append(candidate)
                addNext(temp, total_sum+candidate, candidates[1:])
            elif candidate + total_sum == target:
                temp = stack.copy()
                temp.append(candidate)
                if not temp in result:
                    result.append(temp)
            
            addNext(stack, total_sum, candidates[1:])
        addNext([], 0, candidates)
        return result