# CodeChef: Puppy and Sum (PPSUM)
# https://www.codechef.com/problems/PPSUM
t = int(input())
for _ in range(t):
    d, n = map(int, input().split())
    for _ in range(d):
        n = n * (n + 1) // 2
    print(n)
