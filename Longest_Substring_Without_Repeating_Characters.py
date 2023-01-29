
def lengthOfLongestSubstring(s:str):
    charSet = set()
    l = 0   # l is a left pointer
    result = 0
    for r in range(len(s)):  # r is a right pointer
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        result = max(result, r-l+1)
    return result

s = "abcabcbb"
print(lengthOfLongestSubstring(s))