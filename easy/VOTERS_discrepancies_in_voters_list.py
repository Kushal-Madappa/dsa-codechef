# CodeChef: Discrepancies in the Voters List (VOTERS)
# https://www.codechef.com/problems/VOTERS
from collections import Counter
n1, n2, n3 = map(int, input().split())
c = Counter()
for _ in range(n1 + n2 + n3):
    c[int(input())] += 1
final = sorted(v for v, k in c.items() if k >= 2)
print(len(final))
print('\n'.join(map(str, final)))
