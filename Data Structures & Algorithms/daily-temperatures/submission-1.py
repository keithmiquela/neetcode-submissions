class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack of temp and index
        stack = []
        answers = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not stack:
                stack.append([temp, i])
                continue
            prev_temp = stack[-1][0]
            prev_index = stack[-1][1]
            while temp > prev_temp:
                answers[prev_index] = i - prev_index
                stack.pop()
                if stack:
                    prev_temp = stack[-1][0]
                    prev_index = stack[-1][1]
                else:
                    break
            stack.append([temp, i])

        return answers