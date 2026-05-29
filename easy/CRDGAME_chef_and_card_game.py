# CodeChef: Chef and Card Game (CRDGAME)
# https://www.codechef.com/problems/CRDGAME

def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

t = int(input())
for _ in range(t):
    n = int(input())
    chef = morty = 0
    for _ in range(n):
        a, b = map(int, input().split())
        sa, sb = digit_sum(a), digit_sum(b)
        if sa > sb:
            chef += 1
        elif sa < sb:
            morty += 1
        else:
            chef += 1
            morty += 1
    if chef > morty:
        print(0, chef)
    elif morty > chef:
        print(1, morty)
    else:
        print(2, chef)
