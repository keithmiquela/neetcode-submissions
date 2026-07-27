class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i<j:
            num1 = numbers[i]
            num2 = numbers[j]
            curr_sum = num1 + num2

            if curr_sum<target:
                i+=1
            if curr_sum>target:
                j-=1
            if curr_sum == target:
                return [i+1, j+1]
        return [-1,-1]