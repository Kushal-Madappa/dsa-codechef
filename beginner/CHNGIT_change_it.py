# CodeChef: Change It (CHNGIT)
# https://www.codechef.com/problems/CHNGIT
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for x in a:
        freq[x] = freq.get(x, 0) + 1
    print(n - max(freq.values()))
