# CodeChef: Ciel and Receipt (CIELRCPT)
# https://www.codechef.com/problems/CIELRCPT
# Menu prices are powers of 2 from 1..2048. Greedy from the largest is
# optimal because each item is exactly twice the next, so taking two of
# a smaller coin is never better than one of the next larger.

t = int(input())
for _ in range(t):
    p = int(input())
    count = 0
    for v in (2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1):
        count += p // v
        p %= v
    print(count)
