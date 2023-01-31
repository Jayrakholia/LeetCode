class Solution:
    def searchRange(self, nums, target):
        left_idx = bisect.bisect_left(nums,target)
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1,-1]
        right_idx = bisect.bisect_right(nums,target)-1
        return [left_idx,right_idx]
        