# CodeChef: Chef and Chocolates (CHEFCHOCO)
# https://www.codechef.com/problems/CHEFCHOCO
t = int(input())
for _ in range(t):
    c, x, y = map(int, input().split())
    print((c - x) * y)
