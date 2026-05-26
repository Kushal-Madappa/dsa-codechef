# CodeChef: Grade The Steel (FLOW014)
# https://www.codechef.com/problems/FLOW014
t = int(input())
for _ in range(t):
    parts = input().split()
    h = float(parts[0]); c = float(parts[1]); s = float(parts[2])
    c1 = h > 50
    c2 = c < 0.7
    c3 = s > 5600
    n = c1 + c2 + c3
    if n == 3:
        print(10)
    elif c1 and c2:
        print(9)
    elif c2 and c3:
        print(8)
    elif c1 and c3:
        print(7)
    elif n == 1:
        print(6)
    else:
        print(5)
