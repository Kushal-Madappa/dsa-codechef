# CodeChef: Dominant Element (DOMINANT2)
# https://www.codechef.com/problems/DOMINANT2
from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = Counter(a).most_common()
    if len(freq) == 1 or freq[0][1] > freq[1][1]:
        print("YES")
    else:
        print("NO")
