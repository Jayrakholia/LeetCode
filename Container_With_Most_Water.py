def maxArea(height):
    ans = 0
    left = 0
    right = len(height) - 1

    while left < right:
      minHeight = min(height[left], height[right])
      ans = max(ans, minHeight * (right - left))
      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return ans
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))