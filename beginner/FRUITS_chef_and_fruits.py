# CodeChef: Chef and Fruits (FRUITS)
# https://www.codechef.com/problems/FRUITS
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    d = abs(n - m)
    print(max(0, d - k))
