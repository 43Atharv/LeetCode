class Solution(object):
    def dominantIndex(self, nums):
        n=len(nums)
        fmax=-1
        smax=-1
        fmaxindex=-1
        for i in range(n):
            if(nums[i]>fmax):
                smax=fmax
                fmax=nums[i]
                fmaxindex=i
            elif(nums[i]>smax):
                smax=nums[i]
        if(fmax>=2*smax):
            return fmaxindex
        return -1