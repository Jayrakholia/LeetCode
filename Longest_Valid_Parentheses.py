class Solution:
  def longestValidParentheses(self, s: str) -> int:
    s2 = ')' + s
    lengthOfValid = [0] * len(s2)

    for i in range(1, len(s2)):
      if s2[i] == ')' and s2[i - lengthOfValid[i - 1] - 1] == '(':
        lengthOfValid[i] = lengthOfValid[i - 1] + lengthOfValid[i - lengthOfValid[i - 1] - 2] + 2

    return max(lengthOfValid)