# CodeChef: Smart Phone (ZCO14003)
# https://www.codechef.com/problems/ZCO14003
n = int(input())
b = [int(input()) for _ in range(n)]
b.sort()
ans = 0
for i in range(n):
    rev = b[i] * (n - i)
    if rev > ans:
        ans = rev
print(ans)
