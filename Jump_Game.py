class Solution:
    def canJump(self, nums):
        i =0 
        reach = 0
        while i < len(nums) and i<=reach:
            reach = max(reach, i+nums[i])
            i = i+1
        return i == len(nums)