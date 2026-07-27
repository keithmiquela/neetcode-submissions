class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return 1
        dictionary={}
        for num in nums:
            dictionary[num]=1
        temp_array=sorted(list(dictionary.keys()))
        i=0
        j=0
        max_seq=0
        temp_seq=0
        while i<len(temp_array):
            if j==i:
                temp_seq=1
                j+=1
            elif j<len(temp_array) and temp_array[j]==temp_array[j-1]+1:
                temp_seq+=1
                j+=1
            else:
                i=j
                max_seq=max(max_seq,temp_seq)
        return max_seq
            