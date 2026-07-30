# CodeChef: Chopsticks (TACHSTCK)
# https://www.codechef.com/problems/TACHSTCK
n, d = map(int, input().split())
sticks = sorted(int(input()) for _ in range(n))
pairs = 0
i = 0
while i < n - 1:
    if sticks[i + 1] - sticks[i] <= d:
        pairs += 1
        i += 2
    else:
        i += 1
print(pairs)
