class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        a = 0
        for i in range(len(nums)):
            if nums[i] == 1 :
                 k+=1
                 a = max(a,k)
            else:
                k = 0
        return a


            
