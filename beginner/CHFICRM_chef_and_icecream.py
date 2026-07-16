# CodeChef: Chef and Icecream (CHFICRM)
# https://www.codechef.com/problems/CHFICRM
t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    c5 = c10 = 0
    ok = True
    for x in coins:
        if x == 5:
            c5 += 1
        elif x == 10:
            if c5 == 0:
                ok = False; break
            c5 -= 1
            c10 += 1
        else:  # 15
            if c10 > 0:
                c10 -= 1
            elif c5 >= 2:
                c5 -= 2
            else:
                ok = False; break
    print("YES" if ok else "NO")
