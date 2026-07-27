class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        for num in nums:
            if not dictionary.get(nums.count(num)):
                dictionary[nums.count(num)]= [num]
            else:
                if num not in dictionary[nums.count(num)]:
                    dictionary[nums.count(num)].append(num)
        temp = sorted(dictionary.keys())[::-1]
        total=[]
        for temp_list in temp:
            total= total+dictionary[temp_list]
        result=[]
        for i in range(0,k):
            result.append(total[i])
        return result
        


        