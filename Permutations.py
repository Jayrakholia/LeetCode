class Solution:
    def permute(self, nums):
        def backTrack(first=0):
            if first == len(nums):
                output.append(nums[:])
            for i in range(first,len(nums)):
                nums[first],nums[i] = nums[i],nums[first]
                backTrack(first+1)
                nums[first],nums[i] = nums[i],nums[first]
        output=[]
        backTrack()
        return output