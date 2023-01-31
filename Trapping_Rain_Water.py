class Solution:
  def trap(self, height):
    n = len(height)
    left = 0
    right = n-1
    left_max = 0
    right_max = 0
    result = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                result = result + left_max - height[left]
            left =left+1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                result = result + right_max - height[right]
            right =right-1
    return result 
