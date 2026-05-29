# CodeChef: Two vs Ten (TWOVSTEN)
# https://www.codechef.com/problems/TWOVSTEN
t = int(input())
for _ in range(t):
    x = int(input())
    last = x % 10
    if last == 0:
        print(0)
    elif last == 5:
        print(1)
    else:
        print(-1)
