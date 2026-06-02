# CodeChef: Minimum Maximum (MNMX)
# https://www.codechef.com/problems/MNMX
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print((n - 1) * min(a))
