class Solution:
    def generate(self, numRows):
        ans = []
        for row in range(numRows):
            ans.append ([1]*(row+1))
        for row in range(2,numRows):
            for col in range(1,len(ans[row])-1):
                ans[row][col] = ans[row-1][col-1] + ans[row-1][col]
        return ans