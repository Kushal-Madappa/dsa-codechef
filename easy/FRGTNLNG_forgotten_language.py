# CodeChef: Forgotten Language (FRGTNLNG)
# https://www.codechef.com/problems/FRGTNLNG
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    words = input().split()
    seen = set()
    for _ in range(k):
        parts = input().split()
        seen.update(parts[1:])
    print(' '.join('YES' if w in seen else 'NO' for w in words))
