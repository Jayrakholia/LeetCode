def removeDuplicates(nums):
        i = 0
        for num in nums:
            if i < 1 or num > nums[i - 1]:
                nums[i] = num
                i += 1
        return i
nums= [1,1,2]
print(removeDuplicates(nums))