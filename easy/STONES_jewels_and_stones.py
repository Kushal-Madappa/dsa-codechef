# CodeChef: Jewels and Stones (STONES)
# https://www.codechef.com/problems/STONES
t = int(input())
for _ in range(t):
    jewels = input()
    stones = input()
    js = set(jewels)
    print(sum(1 for c in stones if c in js))
