# CodeChef: Little Elephant and Lemonade (LELEMON)
# https://www.codechef.com/problems/LELEMON
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    visits = list(map(int, input().split()))
    counts = [0] * n
    for v in visits:
        counts[v] += 1
    total = 0
    for i in range(n):
        row = list(map(int, input().split()))
        c = row[0]
        vols = sorted(row[1:1 + c], reverse=True)
        take = min(counts[i], c)
        total += sum(vols[:take])
    print(total)
