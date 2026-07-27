class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(0,len(temperatures)):
            if(len(stack)==0):
                stack.append(i)
                continue
            topIndex = stack[-1]
            while temperatures[topIndex]<temperatures[i]:
                stack.pop()
                result[topIndex]=i-topIndex
                if(len(stack)==0):
                    break;
                topIndex = stack[-1]
            stack.append(i)
        return result

        

