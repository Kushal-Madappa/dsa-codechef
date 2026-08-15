# CodeChef: Mathison and Pangrams (MATPAN)
# https://www.codechef.com/problems/MATPAN
t = int(input())
for _ in range(t):
    cost = list(map(int, input().split()))
    s = input()
    present = set(s)
    total = 0
    for i in range(26):
        if chr(ord('a') + i) not in present:
            total += cost[i]
    print(total)
