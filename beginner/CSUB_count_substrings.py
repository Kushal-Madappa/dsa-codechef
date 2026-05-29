# CodeChef: Count Substrings (CSUB)
# https://www.codechef.com/problems/CSUB
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    c = s.count('1')
    print(c * (c + 1) // 2)
