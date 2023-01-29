def isPalindrome(x: int):
    reverse = 0
    temp = x
    while(x>0):
        dig = x % 10
        reverse = reverse * 10 + dig
        x = x // 10
    return temp == reverse
x = 121
print(isPalindrome(x))