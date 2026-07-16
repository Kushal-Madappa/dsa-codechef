# CodeChef: Add One (ADDONE)
# https://www.codechef.com/practice/course/strings/STRINGS/problems/ADDONE
t = int(input())
for _ in range(t):
    n = input().strip()
    digits = list(n)
    i = len(digits) - 1
    carry = 1
    while i >= 0 and carry:
        d = int(digits[i]) + carry
        digits[i] = str(d % 10)
        carry = d // 10
        i -= 1
    if carry:
        digits = ['1'] + digits
    print(''.join(digits))
