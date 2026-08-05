class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       i = 0
       j = len(nums)-1
       while i<j:
        if nums[i] + nums[j] == target:
            return [i,j]
        for k in range(i + 1, len(nums)):
            if nums[i] + nums[k] == target:
                return [i, k]
        i += 1