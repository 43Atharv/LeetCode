class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []

        output = []
        i=0
        while i< len(nums):
            start = nums[i] #store initial value of i
            while i+1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i+=1
            
            if start == nums[i]:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{nums[i]}")
            
            i+=1
        
        return output