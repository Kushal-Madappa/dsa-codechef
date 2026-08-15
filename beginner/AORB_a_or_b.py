# CodeChef: A or B (AORB)
# https://www.codechef.com/problems/AORB
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    ab = (500 - 2 * x) + (1000 - 4 * (x + y))
    ba = (1000 - 4 * y) + (500 - 2 * (x + y))
    print(max(ab, ba))
