class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_length = len(nums)

        i = 0

        while i < nums_length:
            val_at_i = nums[i]

            belongs_in_range = val_at_i < nums_length

            if belongs_in_range and val_at_i != nums[val_at_i]:
                nums[i], nums[val_at_i] = nums[val_at_i], nums[i]
            else:
                i += 1

        for x in range(nums_length):
            if x != nums[x]:
                return x

        return nums_length