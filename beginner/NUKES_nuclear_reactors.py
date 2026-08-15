# CodeChef: Nuclear Reactors (NUKES)
# https://www.codechef.com/problems/NUKES
a, n, k = map(int, input().split())
base = n + 1
out = []
for _ in range(k):
    out.append(str(a % base))
    a //= base
print(' '.join(out))
