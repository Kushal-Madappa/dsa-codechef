# CodeChef: Little Elephant and Bombs (LEBOMBS)
# https://www.codechef.com/problems/LEBOMBS
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    destroyed = [False] * n
    for i, ch in enumerate(s):
        if ch == '1':
            destroyed[i] = True
            if i > 0:
                destroyed[i - 1] = True
            if i < n - 1:
                destroyed[i + 1] = True
    print(destroyed.count(False))
