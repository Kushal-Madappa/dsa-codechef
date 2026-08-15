# CodeChef: Bella Ciao (CHFHEIST)
# https://www.codechef.com/problems/CHFHEIST
t = int(input())
for _ in range(t):
    D, d, P, Q = map(int, input().split())
    n = D // d
    ans = n * P * d + (Q * n * (n - 1) // 2) * d + (D % d) * (P + n * Q)
    print(ans)
