# CodeChef: Chef and Strings (CHEFSTR1)
# https://www.codechef.com/problems/CHEFSTR1
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        ans += abs(a[i] - a[i-1]) - 1
    print(ans)
